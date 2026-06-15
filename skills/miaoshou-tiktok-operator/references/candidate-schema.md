# Candidate CSV Schema

Use UTF-8 CSV. Keep one row per sellable product or bundle.

## Required Columns

| Column | Meaning |
|---|---|
| `product_name` | Short internal product name |
| `source_url` | Miaoshou or supplier product URL |
| `role` | `traffic`, `profit`, `bundle`, or `test` |
| `sale_price_myr` | Planned TikTok Shop selling price in MYR |
| `product_cost_myr` | Supplier product cost in MYR |
| `shipping_cost_myr` | Seller-paid shipping and fulfillment per order |

## Optional Cost Columns

All currency values use MYR. Percentages use plain percentage numbers, for example `7.5`.

| Column | Default | Meaning |
|---|---:|---|
| `handling_cost_myr` | 0 | Purchasing and China-side handling |
| `packaging_cost_myr` | 0.50 | Packaging |
| `platform_fee_pct` | 8 | TikTok Shop and transaction fees estimate |
| `affiliate_pct` | 10 | Creator affiliate commission |
| `voucher_cost_myr` | 0 | Seller-funded discount |
| `return_allowance_pct` | 5 | Refund and return allowance |
| `ad_allowance_pct` | 0 | Advertising allowance |

## Scoring Columns

Enter integers from 1 to 5. Higher is better except for `risk_score`, where 5 means high risk.

| Column | Default | Meaning |
|---|---:|---|
| `malaysia_fit_score` | 3 | Fit with Malaysian weather and daily use |
| `video_demo_score` | 3 | Ease of showing value in short video |
| `supplier_score` | 3 | Supplier and stock confidence |
| `competition_score` | 3 | Differentiation and competition quality |
| `risk_score` | 3 | Compliance, IP, return, and fulfillment risk |

## Example

```csv
product_name,source_url,role,sale_price_myr,product_cost_myr,shipping_cost_myr,handling_cost_myr,packaging_cost_myr,platform_fee_pct,affiliate_pct,voucher_cost_myr,return_allowance_pct,ad_allowance_pct,malaysia_fit_score,video_demo_score,supplier_score,competition_score,risk_score
3-pair quick-dry socks,https://example.com/item/1,traffic,16.90,3.20,4.00,0.50,0.50,8,10,1.00,5,0,5,4,4,3,2
```
