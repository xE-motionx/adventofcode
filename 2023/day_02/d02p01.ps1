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
$maxRedCubes = 12
$maxGreenCubes = 13
$maxBlueCubes = 14
$final = 0

# <-- main -->
$data = Get-Content -Path $dataSource
foreach($game in $data){
    $r, $b, $g = 0,0,0
    $set = $game.split(":")
    $draws = ($set[1].split(";"))
    Write-Host " # --> $($set[0]) (" -NoNewLine
    foreach($draw in $draws){
        $splits = $draw.split(",").trim(" ")
        foreach($part in $splits){
            if ($part.split(" ")[1] -eq "red"){
                $r += $part.split(" ")[0]
            }
            if ($part.split(" ")[1] -eq "green"){
                $g += $part.split(" ")[0]
            }
            if ($part.split(" ")[1] -eq "blue"){
                $b += $part.split(" ")[0]
            }
        }
    }
    Write-Host "Red: $($r), Green: $($g), Blue: $($b)) " -NoNewLine
    if($r -le $maxRedCubes -and $b -le $maxBlueCubes -and $g -le $maxGreenCubes) {
        Write-Host "Legit."
        $final += [int] $set[0].split(" ")[1]
    } else {
        Write-Host "Illegal."
    }
}
Write-Host "Final: $($final)"