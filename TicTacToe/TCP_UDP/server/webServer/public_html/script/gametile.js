"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class GameTile {
    constructor(gameField, coords) {
        this.gameField = gameField;
        this.coords = coords;
    }
    occupy(player) {
        this.occupier = player;
    }
    getSign() {
        return this.occupier.sign;
    }
}
exports.default = GameTile;
