#include <iostream>
#include <vector>

void print_vector(std::vector<int> A)
{
    std::cout << "Vector contents: ";
    for (size_t i = 0; i < A.size(); ++i) {
        std::cout << A[i];
        if (i < A.size() - 1) {
            std::cout << ", "; // Add a comma and space between elements
        }
    }
    std::cout << std::endl;
    return;
}
