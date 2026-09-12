param(
    [Parameter(Mandatory = $true)]
    [string]$Url
)

$ErrorActionPreference = "Stop"

try {
    $started = Get-Date
    $response = Invoke-WebRequest -Uri $Url -Method Get -TimeoutSec 15
    $elapsed = ((Get-Date) - $started).TotalMilliseconds

    [PSCustomObject]@{
        Url        = $Url
        StatusCode = [int]$response.StatusCode
        LatencyMs  = [math]::Round($elapsed, 0)
        Healthy    = $response.StatusCode -ge 200 -and $response.StatusCode -lt 400
    } | Format-List
}
catch {
    Write-Error "Health check failed: $($_.Exception.Message)"
    exit 1
}
