1/**
2 * @param {string} s
3 * @param {string} t
4 * @return {boolean}
5 */
6var isAnagram = function(s, t) {
7    if(s.length!==t.length) return false;
8    let alpha = new Array(26).fill(0);
9    const acode='a'.charCodeAt(0);
10    for(let i=0;i<s.length;i++){
11        alpha[s.charCodeAt(i)-acode]++;
12        alpha[t.charCodeAt(i)-acode]--;
13
14    }
15    return alpha.every(x => x==0)
16
17
18    
19};