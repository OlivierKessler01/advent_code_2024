#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include "utils.h"

std::vector<std::vector<int>> offsets = {
    {-1,-1},
    {1,1},
    {1,-1},
    {-1,1},
};

void find_xmas(std::vector<std::vector<char>> &matrix, int i, int j, int &answer){
    char top_left, top_right, bottom_left, bottom_right;

    if ((i < 1 || i > matrix.size() -2) || (j < 1 || j > matrix[0].size() -2))
        return;
    
    top_left = matrix[i-1][j-1];
    top_right = matrix[i-1][j+1];
    bottom_left = matrix[i+1][j-1];
    bottom_right = matrix[i+1][j+1];

    if (
        (top_left == 'M' and top_right == 'M' and bottom_left == 'S' and bottom_right == 'S') ||
        (top_left == 'S' and top_right == 'S' and bottom_left == 'M' and bottom_right == 'M') ||
        (top_left == 'M' and top_right == 'S' and bottom_left == 'M' and bottom_right == 'S') ||
        (top_left == 'S' and top_right == 'M' and bottom_left == 'S' and bottom_right == 'M')
    )
        answer+=1;

    return;
}

void solve(std::vector<std::vector<char>> &matrix, int &answer)
{
    std::cout << "Size matrix : " << matrix.size() << " * " << matrix[0].size() << std::endl;

    for(int i = 0 ; i< matrix.size();i++){
        for(int j = 0; j<matrix[0].size();j++){
            if (matrix[i][j] == 'A'){
                find_xmas(matrix,i,j,answer);
            }
        }
    }    

    return;
}

int main(int argc, char** argv)
{
    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    int answer = 0;
    std::vector<char> report;
    std::vector<std::vector<char>> matrix;

    fp = fopen("day_4.data", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);
    
    while ((read = getline(&line, &len, fp)) != -1) {
        printf("Retrieved line of length %zu:\n", read);
        printf("%s", line);
        report = {};

        for (int index = 0; index < read -1 ; index++) {
            report.push_back(line[index]);
        }

        matrix.push_back(report);
    }

    fclose(fp);
    if (line)
        free(line);

    //for(auto line: matrix){
     //   print_vector(line);
    //}
    solve(matrix,answer);
    std::cout << answer << std::endl;

    exit(EXIT_SUCCESS);
}
