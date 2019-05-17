#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    vector<int> queue;
    bool isSorted = true;
    for(string comm:operations){
        stringstream ss(comm);
        string c,value;
        ss>>c>>value;
        if(c == "I"){
            queue.push_back(stoi(value));
            isSorted = false;
        }else if(c=="D"){
            if(queue.size()==0){
                continue;
            }
            if (isSorted == false){
                sort(queue.begin(),queue.end());
                isSorted = true;
            }
            if(value=="1"){
                queue.pop_back();
            }else if(value=="-1"){
                queue.erase(queue.begin());
            }
        }
    }
    if (queue.size()==0){
        answer.push_back(0);
        answer.push_back(0);
    }else{
        if(isSorted==false)
            sort(queue.begin(),queue.end());
        answer.push_back(queue.back());
        answer.push_back(queue.front());
    }
    return answer;
}