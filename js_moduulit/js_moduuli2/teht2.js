'use strict';
const numberOfCandidates = Number(
    prompt('How many candidates?')
);

const candidates = [];
for (let i = 0; i < numberOfCandidates; i++) {

    const name = prompt(`Name for candidate ${i + 1}`);
    const candidate = {
        name: name,
        votes: 0
    };
    candidates.push(candidate);
}

const numberOfVoters = Number(
    prompt('How many voters?')
);

for (let i = 0; i < numberOfVoters; i++) {
    const vote = prompt(`Who do you vote for?`);
    if (vote === '') {
        continue;
    }
    const candidate = candidates.find(
        candidate => candidate.name.toLowerCase() === vote.toLowerCase()
    );
    if (candidate) {
        candidate.votes++;
    }
}

candidates.sort((a, b) => b.votes - a.votes);

const winner = candidates[0];

if (winner) {
    console.log(
        `The winner is ${winner.name} with ${winner.votes} votes.`
    );

    console.log('results:');
    for (const candidate of candidates) {
        console.log(`${candidate.name}: ${candidate.votes} votes`);
    }
} 
else {
    console.log('No candidates.');
}
