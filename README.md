# 我的 Codex Skills

这里保存我创建并愿意共享的 Codex Skills。每个 Skill 都是一个独立文件夹，可以单独复制、安装或分享。

## 当前 Skills

### miaoshou-tiktok-operator

用于妙手 ERP 与 TikTok Shop Malaysia 的选品、利润核算、商品资料准备和审核后上架。

主要能力：

- 从妙手 ERP 中收集候选商品
- 按马来西亚市场适配度筛选
- 估算平台费用、达人佣金、物流、退款和单件利润
- 生成 TikTok Shop 商品资料
- 先保存草稿，确认后再发布
- 排除侵权、高风险和明显亏损商品

位置：`skills/miaoshou-tiktok-operator`

## 安装

### 从 GitHub 安装

仓库上传 GitHub 后，把仓库链接发给 Codex，然后说：

```text
请从这个 GitHub 仓库安装 skills/miaoshou-tiktok-operator：
https://github.com/wendysun718/my-codex-skills
```

Codex 会使用 Skill 安装流程处理。也可以下载仓库 ZIP，再手动安装对应文件夹。

### 手动安装

将整个 `skills/miaoshou-tiktok-operator` 文件夹复制到：

```text
~/.codex/skills/miaoshou-tiktok-operator
```

然后重启 Codex。

## 使用示例

```text
使用 $miaoshou-tiktok-operator，从我已经登录的妙手 ERP 中寻找
20款适合马来西亚的户外商品。先计算利润并生成候选名单，不要上架。
```

## 安全说明

- 仓库中不得保存账号、密码、验证码、Cookie、访问令牌或真实店铺 ID。
- 正式上传前，应再次搜索个人路径、邮箱、手机号、店铺名称和访问凭证。
- 使用者应通过自己已经登录的网页会话完成操作。
- 商品正式发布前应核对目标店铺、售价、库存、利润和商品合规性。
- 本 Skill 不使用妙手 ERP 的非公开接口，不保证第三方网页改版后仍能完全自动操作。

## 许可

本仓库使用 MIT License。其他人可以使用、修改和分发，但需保留许可声明。
