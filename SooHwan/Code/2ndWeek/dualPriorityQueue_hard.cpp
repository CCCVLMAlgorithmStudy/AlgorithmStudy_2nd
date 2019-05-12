#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <algorithm>
#include <sstream>
using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    priority_queue<int,vector<int>,less<int>> maxQ;
    priority_queue<int,vector<int>,greater<int>> minQ;
    
    for(string comm:operations){
        stringstream ss(comm);
        string c,value;
        ss>>c>>value;
        if (c== "I"){
            maxQ.push(stoi(value));
        }
        else if (c=="D"){
            if(maxQ.size()==0&&minQ.size()==0){
                continue;
            }
            if(value == "1"){
                if(maxQ.size()==0){
                    if(minQ.size()==1){
                        maxQ.push(minQ.top());
                        minQ.pop();
                    }else{
                        vector<int> temp;
                        int s = minQ.size();
                        for(int i = 0;i<(s+1)/2;i++){
                            temp.push_back(minQ.top());
                            minQ.pop();
                        }
                        while(minQ.size()!=0){
                            maxQ.push(minQ.top());
                            minQ.pop();
                        }
                        while(temp.size()!=0){
                            minQ.push(temp.back());
                            temp.pop_back();
                        }
                    }
                }
                maxQ.pop();
            }
            else if(value == "-1"){
                if(minQ.size()==0){
                    if(maxQ.size()==1){
                        minQ.push(maxQ.top());
                        maxQ.pop();
                    }
                    vector<int> temp;
                    int s = maxQ.size();
                    for(int i = 0;i<(s+1)/2;i++){
                        temp.push_back(maxQ.top());
                        maxQ.pop();
                    }
                    while(maxQ.size()!=0){
                        minQ.push(maxQ.top());
                        maxQ.pop();
                    }
                    while(temp.size()!=0){
                        maxQ.push(temp.back());
                        temp.pop_back();
                    }
                }
                minQ.pop();
                
            }
        }
    }
    
    if(minQ.size()==0&&maxQ.size()==0){
        answer.push_back(0);
        answer.push_back(0);
    }else if(maxQ.size()==0){
        answer.push_back(minQ.top());
        if(minQ.size()==1){
            answer.push_back(minQ.top());
        }else{
            vector<int> temp;
            int s = minQ.size();
            for(int i = 0;i<(s+1)/2;i++){
                temp.push_back(minQ.top());
                minQ.pop();
            }
            while(minQ.size()!=0){
                maxQ.push(minQ.top());
                minQ.pop();
            }
            while(temp.size()!=0){
                minQ.push(temp.back());
                temp.pop_back();
            }
            answer.push_back(maxQ.top());
            reverse(answer.begin(),answer.end());
            }
    }else if(minQ.size()==0){
        answer.push_back(maxQ.top());
        if (maxQ.size()==1){
            answer.push_back(maxQ.top());
        }else{
            vector<int> temp;
            int s = maxQ.size();
            for(int i = 0;i<(s+1)/2;i++){
                temp.push_back(maxQ.top());
                maxQ.pop();
            }
            while(maxQ.size()!=0){
                minQ.push(maxQ.top());
                maxQ.pop();
            }
            while(temp.size()!=0){
                maxQ.push(temp.back());
                temp.pop_back();
            }
            answer.push_back(minQ.top());
        }
    }else{
        answer.push_back(maxQ.top());
        answer.push_back(minQ.top());
    }
    
    return answer;
}