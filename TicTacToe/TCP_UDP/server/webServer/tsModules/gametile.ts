import GameField from "./tictactoe";
import Player,{Sign} from "./player";
export default class GameTile {
    gameField: GameField;
    coords: [number, number];
    occupier: Player;
    constructor(gameField: GameField, coords: [number, number]) {
        this.gameField = gameField;
        this.coords = coords;
    }
    occupy(player: Player) {
        this.occupier = player;
    }
    getSign():Sign{
        return this.occupier.sign;
    }
}