#!/usr/bin/env python3
"""Score Miaoshou product candidates and estimate contribution profit."""

import argparse
import csv
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path


MONEY = Decimal("0.01")


def number(row, key, default):
    value = row.get(key, "")
    if value is None or str(value).strip() == "":
        return Decimal(str(default))
    try:
        return Decimal(str(value).strip())
    except InvalidOperation as exc:
        raise ValueError(f"{key} must be a number, got {value!r}") from exc


def bounded_score(row, key, default=3):
    value = number(row, key, default)
    if value < 1 or value > 5:
        raise ValueError(f"{key} must be between 1 and 5, got {value}")
    return value


def money(value):
    return value.quantize(MONEY, rounding=ROUND_HALF_UP)


def score_row(row):
    sale = number(row, "sale_price_myr", 0)
    if sale <= 0:
        raise ValueError("sale_price_myr must be greater than zero")

    fixed_cost = sum(
        (
            number(row, "product_cost_myr", 0),
            number(row, "shipping_cost_myr", 0),
            number(row, "handling_cost_myr", 0),
            number(row, "packaging_cost_myr", 0.5),
            number(row, "voucher_cost_myr", 0),
        ),
        Decimal("0"),
    )
    percentage_cost = sale * sum(
        (
            number(row, "platform_fee_pct", 8),
            number(row, "affiliate_pct", 10),
            number(row, "return_allowance_pct", 5),
            number(row, "ad_allowance_pct", 0),
        ),
        Decimal("0"),
    ) / Decimal("100")

    total_cost = fixed_cost + percentage_cost
    profit = sale - total_cost
    margin = profit / sale * Decimal("100")

    malaysia_fit = bounded_score(row, "malaysia_fit_score")
    video_demo = bounded_score(row, "video_demo_score")
    supplier = bounded_score(row, "supplier_score")
    competition = bounded_score(row, "competition_score")
    risk = bounded_score(row, "risk_score")

    commercial_score = max(Decimal("0"), min(Decimal("5"), margin / Decimal("8")))
    final_score = (
        malaysia_fit * Decimal("0.22")
        + video_demo * Decimal("0.18")
        + supplier * Decimal("0.14")
        + competition * Decimal("0.12")
        + commercial_score * Decimal("0.24")
        + (Decimal("6") - risk) * Decimal("0.10")
    )

    role = (row.get("role") or "test").strip().lower()
    min_profit = Decimal("4") if role == "traffic" else Decimal("8")
    if profit < 0:
        decision = "reject-loss"
    elif margin < 20:
        decision = "hold-low-margin"
    elif profit < min_profit:
        decision = "hold-low-profit"
    elif risk >= 4:
        decision = "manual-risk-review"
    elif final_score >= Decimal("3.8"):
        decision = "shortlist"
    else:
        decision = "test-only"

    result = dict(row)
    result.update(
        {
            "estimated_total_cost_myr": f"{money(total_cost):.2f}",
            "estimated_profit_myr": f"{money(profit):.2f}",
            "estimated_margin_pct": f"{money(margin):.2f}",
            "selection_score_5": f"{money(final_score):.2f}",
            "decision": decision,
        }
    )
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input candidate CSV")
    parser.add_argument("--output", required=True, help="Output scored CSV")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    with input_path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        if not reader.fieldnames:
            raise SystemExit("Input CSV has no header")
        rows = []
        for line_number, row in enumerate(reader, start=2):
            try:
                rows.append(score_row(row))
            except ValueError as exc:
                raise SystemExit(f"Line {line_number}: {exc}") from exc

    extra_fields = [
        "estimated_total_cost_myr",
        "estimated_profit_myr",
        "estimated_margin_pct",
        "selection_score_5",
        "decision",
    ]
    fieldnames = list(reader.fieldnames) + [
        field for field in extra_fields if field not in reader.fieldnames
    ]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as target:
        writer = csv.DictWriter(target, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Scored {len(rows)} products -> {output_path}")


if __name__ == "__main__":
    main()
