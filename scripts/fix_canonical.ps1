$siteDir = 'C:\Users\Administrator\.qclaw\workspace\calcwithme-site'
$files = Get-ChildItem $siteDir -Recurse -Filter '*.html'
$count = 0
foreach ($f in $files) {
    $content = Get-Content $f.FullName -Raw -Encoding UTF8
    if ($content -match 'subtle-kelpie') {
        $newContent = $content -replace 'https://subtle-kelpie-9a9a41.netlify.app/', 'https://calcwithme.com/'
        [System.IO.File]::WriteAllText($f.FullName, $newContent)
        $count++
    }
}
Write-Host "Fixed $count files"
