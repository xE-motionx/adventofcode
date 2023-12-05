#.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.
# Author: Frederik Brönner
# Date: 2023.12.04
# AOC:  02
# Problem description:
#   Predict if a set of rolls is legitimate under given
#   circumstances.
#.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.

# <-- imports -->

# <-- functions -->

# <-- vars -->
$dataSource = "./input" # "./input" # "./example"
$final = 0

# <-- main -->
$data = Get-Content -Path $dataSource
foreach($game in $data){
    $r, $b, $g = 0,0,0
    $set = $game.split(":")
    $draws = ($set[1].split(";"))
    $power = 0
    Write-Host " # $($set[0]) " -NoNewLine
    foreach($draw in $draws){
        $splits = $draw.split(",").trim(" ")
        foreach($part in $splits){
            if ($part.split(" ")[1] -eq "red" -and [int] $part.split(" ")[0] -gt $r){
                $r = [int] $part.split(" ")[0]
            }
            if ($part.split(" ")[1] -eq "green" -and [int] $part.split(" ")[0] -gt $g){
                $g = [int] $part.split(" ")[0]
            }
            if ($part.split(" ")[1] -eq "blue" -and [int] $part.split(" ")[0] -gt $b){
                $b = [int] $part.split(" ")[0]
            }
        }
    }
    Write-Host "--> Red: $($r), Green: $($g), Blue: $($b)" -NoNewLine
    $power = $r * $g * $b
    Write-host "--> Power $($power)"
    $final += $power
}
Write-Host "Final: $($final)"
