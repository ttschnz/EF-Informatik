"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const gametile_1 = require("./gametile");
class GameField {
    /**
     *
     * @param size width and height of the field
     * @param players attacker and defender
     */
    constructor(size, players) {
        // save properties
        this.size = size;
        this.attacker = players[0];
        this.defender = players[1];
        // build grid
        this.grid = [];
        for (let i = 0; i < this.size[0]; i++) {
            let row = new Array();
            for (let j = 0; j < this.size[1]; j++) {
                row.push(new gametile_1.default(this, [i, j]));
            }
            this.grid.push(row);
        }
        // initialize players
        this.attacker.assignGameField(this);
        this.defender.assignGameField(this);
    }
}
exports.default = GameField;
