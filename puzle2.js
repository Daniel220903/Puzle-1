function Puzle2() {
    function isHex(hexNum) {
        const numStr = hexNum.toString(16);
        const longitud = numStr.length;
        
        const indexMed = Math.floor(longitud / 2);

        if (numStr[indexMed] !== '3') {
            return false;
        }

        for (let j = 1; j <= longitud; j++) {
            const subNum = parseInt(numStr.slice(0, j), 16); 
            if (subNum % j !== (j - 1)) {
                return false;
            }
        }
        return true;
    }

    let hexNum = 1;
    let longestNum = 0;

    while (hexNum <= 10000) {
        if (isHex(hexNum))
            longestNum = hexNum;
        hexNum++;
    }

    return longestNum.toString(16);
}

console.log(Puzle2());
