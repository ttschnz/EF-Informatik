import GameField from "./tictactoe";

export default class Player {
    sign:Sign;
    gameField:GameField;
    assignGameField(gameField:GameField){
        this.gameField = gameField;
    }
    makeMove(){
    
    }
}

interface SignsDictonary {
    numberToText: Function,
    textToNumber: Function
}

export const SIGNS: SignsDictonary = {
    numberToText(n: number): string {
        switch (n) {
            case -1:
                return "x";
            case 1:
                return "o";
            case 0:
                return "□";
        }
    },
    textToNumber(s: string): number {
        switch (s) {
            case "x":
                return -1;
            case "o":
                return 1;
            case "□":
                return 0;
        }
    }
}

export interface Sign {
    numberValue: number;
    textValue: "x" | "o" | "□";
}