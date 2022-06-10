input.onButtonPressed(Button.A, function () {
    isPlaying = !(isPlaying)
})
function test_function () {
    basic.showIcon(IconNames.Heart)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
}
let isPlaying = false
isPlaying = false
basic.forever(function () {
    while (isPlaying) {
        music.playMelody("E B C5 A B G A F ", 120)
    }
})
