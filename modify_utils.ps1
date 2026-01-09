# 读取文件
$lines = Get-Content utils.py -Encoding UTF8

# 准备要插入的日志代码
$logCode = @"
        # 🔍 输出完整的 API 返回内容
        print("\n" + "="*80)
        print("🔍 官方 API 完整返回内容 (JSON 格式)")
        print("="*80)
        import json
        print(json.dumps(response_data, indent=2, ensure_ascii=False))
        print("="*80 + "\n")
        
"@

# 在第 254 行（try:）之后插入
$newLines = @()
for ($i = 0; $i -lt $lines.Count; $i++) {
    $newLines += $lines[$i]
    if ($i -eq 253) {  # 第 254 行的索引是 253
        $newLines += $logCode
    }
}

# 写回文件
$newLines | Set-Content utils.py -Encoding UTF8
Write-Host "✅ 日志代码已成功添加到 utils.py"
