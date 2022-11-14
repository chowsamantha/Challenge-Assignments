import os
import csv

election_csv = os.path.join("Resources","election_data.csv")

with open(election_csv) as election:
    csv_reader = csv.reader(election,delimiter=",")
    csv_header = next(election)

    data = list(csv_reader)
    NoVotes = len(data)

    CandidateList = []
    Count = []

    for i in range (0,NoVotes):
        Candidate = data[i][2]
        Count.append(Candidate)
        if Candidate not in CandidateList:
            CandidateList.append(Candidate)
    CandidateCount = len(CandidateList)

    Votes = []
    PercentVote = []
    for j in range (0,CandidateCount):
        Name = CandidateList[j]
        Votes.append(Count.count(Name))
        Perc = Votes[j]/NoVotes
        PercentVote.append(Perc)
    
    Winner = Votes.index(max(Votes))

    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {NoVotes}")
    print("---------------------------")
    for k in range (0,CandidateCount):
        print(f"{CandidateList[k]}, {PercentVote[k]:.3%} ({Votes[k]:,})")
    print("---------------------------")
    print(f"Winner: {CandidateList[Winner]}")
    print("---------------------------")

filepath = os.path.join("Analysis","ElectionResults.txt")
with open(filepath,"w") as textfile:
    print("Election Results", file=textfile)
    print("---------------------------", file=textfile)
    print(f"Total Votes: {NoVotes}", file=textfile)
    print("---------------------------", file=textfile)
    for k in range (0,CandidateCount):
        print(f"{CandidateList[k]}, {PercentVote[k]:.3%} ({Votes[k]:,})", file=textfile)
    print("---------------------------", file=textfile)
    print(f"Winner: {CandidateList[Winner]}", file=textfile)
    print("---------------------------", file=textfile)