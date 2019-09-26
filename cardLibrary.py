red, green, blue, white, black, yellow = 'red', 'green', 'blue', 'white', 'black', 'yellow'
requirements = 'requirements'
points = 'points'

cardsInDeckLv1 = {
    red:{
        'red000':{requirements:{red:2, green:0, blue:0, white:2, black:0}, points:0},
        'red001':{requirements:{red:0, green:1, blue:2, white:0, black:0}, points:0},
        'red002':{requirements:{red:0, green:1, blue:0, white:2, black:2}, points:0},
        'red003':{requirements:{red:1, green:0, blue:0, white:1, black:3}, points:0},
        'red004':{requirements:{red:0, green:0, blue:0, white:3, black:0}, points:0},
        'red005':{requirements:{red:0, green:1, blue:1, white:2, black:1}, points:0},
        'red006':{requirements:{red:0, green:1, blue:1, white:1, black:1}, points:0},
        'red007':{requirements:{red:0, green:0, blue:0, white:4, black:0}, points:1},
    },
    green:{
        'green000':{requirements:{red:1, green:0, blue:1, white:1, black:1}, points:0},
        'green001':{requirements:{red:0, green:1, blue:3, white:1, black:0}, points:0},
        'green002':{requirements:{red:1, green:0, blue:1, white:1, black:2}, points:0},
        'green003':{requirements:{red:2, green:0, blue:1, white:0, black:2}, points:0},
        'green004':{requirements:{red:3, green:0, blue:0, white:0, black:0}, points:0},
        'green005':{requirements:{red:0, green:0, blue:1, white:2, black:0}, points:0},
        'green006':{requirements:{red:2, green:0, blue:2, white:0, black:0}, points:0},
        'green007':{requirements:{red:0, green:0, blue:0, white:0, black:4}, points:1},

    },
    blue:{
        'blue000':{requirements:{red:0, green:2, blue:0, white:0, black:2}, points:0},
        'blue001':{requirements:{red:2, green:2, blue:0, white:1, black:0}, points:0},
        'blue002':{requirements:{red:2, green:1, blue:0, white:1, black:1}, points:0},
        'blue003':{requirements:{red:1, green:3, blue:1, white:0, black:0}, points:0},
        'blue004':{requirements:{red:1, green:1, blue:0, white:1, black:1}, points:0},
        'blue005':{requirements:{red:0, green:0, blue:0, white:1, black:2}, points:0},
        'blue006':{requirements:{red:0, green:0, blue:0, white:0, black:3}, points:0},
        'blue007':{requirements:{red:4, green:0, blue:0, white:0, black:0}, points:1},

    },
    white:{
        'white000':{requirements:{red:1, green:2, blue:1, white:0, black:1}, points:0},
        'white001':{requirements:{red:0, green:0, blue:2, white:0, black:2}, points:0},
        'white002':{requirements:{red:1, green:1, blue:1, white:0, black:1}, points:0},
        'white003':{requirements:{red:0, green:0, blue:1, white:3, black:1}, points:0},
        'white004':{requirements:{red:0, green:2, blue:2, white:0, black:1}, points:0},
        'white005':{requirements:{red:2, green:0, blue:0, white:0, black:1}, points:0},
        'white006':{requirements:{red:0, green:0, blue:3, white:0, black:0}, points:0},
        'white007':{requirements:{red:0, green:4, blue:0, white:0, black:0}, points:1},
    },
    black:{
        'black000':{requirements:{red:1, green:0, blue:2, white:2, black:0}, points:0},
        'black001':{requirements:{red:1, green:2, blue:0, white:0, black:0}, points:0},
        'black002':{requirements:{red:3, green:1, blue:0, white:0, black:1}, points:0},
        'black003':{requirements:{red:0, green:2, blue:0, white:2, black:0}, points:0},
        'black004':{requirements:{red:1, green:1, blue:2, white:1, black:0}, points:0},
        'black005':{requirements:{red:0, green:3, blue:0, white:0, black:0}, points:0},
        'black006':{requirements:{red:1, green:1, blue:1, white:1, black:0}, points:0},
        'black007':{requirements:{red:0, green:0, blue:4, white:0, black:0}, points:1},

    }
}


cardsInDeckLv2 = {
    red:{
        'red008':{requirements:{red:2, green:0, blue:0, white:2, black:3}, points:1},
        'red009':{requirements:{red:2, green:0, blue:3, white:0, black:3}, points:1},
        'red010':{requirements:{red:0, green:2, blue:4, white:1, black:0}, points:2},
        'red011':{requirements:{red:0, green:0, blue:0, white:0, black:5}, points:2},
        'red012':{requirements:{red:0, green:0, blue:0, white:3, black:5}, points:2},
        'red013':{requirements:{red:6, green:0, blue:0, white:0, black:0}, points:3},

    },
    green:{
        'green008':{requirements:{red:3, green:2, blue:0, white:3, black:0}, points:1},
        'green009':{requirements:{red:0, green:0, blue:3, white:2, black:2}, points:1},
        'green010':{requirements:{red:0, green:0, blue:2, white:4, black:1}, points:2},
        'green011':{requirements:{red:0, green:5, blue:0, white:0, black:0}, points:2},
        'green012':{requirements:{red:0, green:3, blue:5, white:0, black:0}, points:2},
        'green013':{requirements:{red:0, green:6, blue:0, white:0, black:0}, points:3},
    },
    blue:{
        'blue008':{requirements:{red:0, green:3, blue:2, white:0, black:3}, points:1},
        'blue009':{requirements:{red:3, green:2, blue:2, white:0, black:0}, points:1},
        'blue010':{requirements:{red:0, green:0, blue:5, white:0, black:0}, points:2},
        'blue011':{requirements:{red:1, green:0, blue:0, white:2, black:4}, points:2},
        'blue012':{requirements:{red:0, green:0, blue:3, white:5, black:0}, points:2},
        'blue013':{requirements:{red:0, green:0, blue:6, white:0, black:0}, points:3},
    },
    white:{
        'white008':{requirements:{red:2, green:3, blue:0, white:0, black:2}, points:1},
        'white009':{requirements:{red:3, green:0, blue:3, white:2, black:0}, points:1},
        'white010':{requirements:{red:5, green:0, blue:0, white:0, black:3}, points:2},
        'white011':{requirements:{red:5, green:0, blue:0, white:0, black:0}, points:2},
        'white012':{requirements:{red:4, green:1, blue:0, white:0, black:2}, points:2},
        'white013':{requirements:{red:0, green:0, blue:0, white:6, black:0}, points:3},
    },
    black:{
        'black008':{requirements:{red:0, green:3, blue:0, white:3, black:2}, points:1},
        'black009':{requirements:{red:0, green:2, blue:2, white:3, black:0}, points:1},
        'black010':{requirements:{red:3, green:5, blue:0, white:0, black:0}, points:2},
        'black011':{requirements:{red:2, green:4, blue:1, white:0, black:0}, points:2},
        'black012':{requirements:{red:0, green:0, blue:0, white:5, black:0}, points:2},
        'black013':{requirements:{red:0, green:0, blue:0, white:0, black:6}, points:3},
    }
}


cardsInDeckLv3 = {
    red:{
        'red014':{requirements:{red:0, green:3, blue:5, white:3, black:3}, points:3},
        'red015':{requirements:{red:0, green:7, blue:0, white:0, black:0}, points:4},
        'red016':{requirements:{red:3, green:6, blue:3, white:0, black:0}, points:4},
        'red017':{requirements:{red:3, green:7, blue:0, white:0, black:0}, points:5},
    },
    green:{
        'green014':{requirements:{red:3, green:0, blue:3, white:5, black:3}, points:3},
        'green015':{requirements:{red:0, green:3, blue:6, white:3, black:0}, points:4},
        'green016':{requirements:{red:0, green:0, blue:7, white:0, black:0}, points:4},
        'green017':{requirements:{red:0, green:3, blue:7, white:0, black:0}, points:5},
    },
    blue:{
        'blue014':{requirements:{red:3, green:3, blue:0, white:3, black:5}, points:3},
        'blue015':{requirements:{red:0, green:0, blue:0, white:7, black:0}, points:4},
        'blue016':{requirements:{red:0, green:0, blue:3, white:6, black:3}, points:4},
        'blue017':{requirements:{red:0, green:0, blue:3, white:7, black:0}, points:5},
    },
    white:{
        'white014':{requirements:{red:5, green:3, blue:3, white:0, black:3}, points:3},
        'white015':{requirements:{red:3, green:0, blue:0, white:3, black:6}, points:4},
        'white016':{requirements:{red:0, green:0, blue:0, white:0, black:7}, points:4},
        'white017':{requirements:{red:0, green:0, blue:0, white:3, black:7}, points:5},
    },
    black:{
        'black014':{requirements:{red:3, green:5, blue:3, white:3, black:0}, points:3},
        'black015':{requirements:{red:6, green:3, blue:0, white:0, black:3}, points:4},
        'black016':{requirements:{red:7, green:0, blue:0, white:0, black:0}, points:4},
        'black017':{requirements:{red:7, green:0, blue:0, white:0, black:3}, points:5},
    },
}