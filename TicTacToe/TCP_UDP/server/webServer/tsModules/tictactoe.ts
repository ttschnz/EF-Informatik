import Player from "./player";
import GameTile from "./gametile";
import {
    Sign
} from "./player";
export default class GameField {
    size: [number, number];
    attacker: Player;
    defender: Player;
    grid: Array < Array < GameTile >> ;
    /**
     * 
     * @param size width and height of the field
     * @param players attacker and defender
     */
    constructor(size: [number, number], players: [Player, Player], ) {
        // save properties
        this.size = size;
        this.attacker = players[0];
        this.defender = players[1];

        // build grid
        this.grid = [];
        for (let i: number = 0; i < this.size[0]; i++) {
            let row: Array < GameTile > = new Array();
            for (let j: number = 0; j < this.size[1]; j++) {
                row.push(new GameTile(this, [i, j]));
            }
            this.grid.push(row);
        }

        // initialize players
        this.attacker.assignGameField(this);
        this.defender.assignGameField(this);
    }

    gameEnded(): boolean {
        return Boolean(this.getWinningPlayer());
    }

    getWinningPlayer(): Player | false {
        // check horizontally
        for (let i of this.grid) {
            let firstItem: Player = i[0].occupier;
            let winningRow: Boolean = true;
            for (let j of i) {
                if (j.occupier == firstItem) winningRow = false;
            }
            if (winningRow == true) return firstItem;
        }

        // check vertically
        for (let i of this.grid.map((_: GameTile[], index: number, arr: GameTile[][]) => {
                return arr.map((item: GameTile[]) => {
                    return item[index]
                })
            })) { // rotate grid by 90 degrees
            let firstItem: Player = i[0].occupier;
            let winningRow: Boolean = true;
            for (let j of i) {
                if (j.occupier == firstItem) winningRow = false;
            }
            if (winningRow == true) return firstItem;
        }

        // check diagonally
        for(let i = 0; i<this.grid.length; i+=1){
            for(let j = 0; j<2; j+=1){
                
            }
        }


        return false;
    }

    start(): void {
        let nextPlayer: Player = this.attacker;
        while (!this.gameEnded()) {
            nextPlayer.makeMove();
            nextPlayer = this.attacker == nextPlayer ? this.defender : this.attacker;
        }
        this.getWinningPlayer()
    }
}