"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.SIGNS = void 0;
class Player {
    assignGameField(gameField) {
        this.gameField = gameField;
    }
}
exports.default = Player;
exports.SIGNS = {
    numberToText(n) {
        switch (n) {
            case -1:
                return "x";
            case 1:
                return "o";
            case 0:
                return "□";
        }
    },
    textToNumber(s) {
        switch (s) {
            case "x":
                return -1;
            case "o":
                return 1;
            case "□":
                return 0;
        }
    }
};
