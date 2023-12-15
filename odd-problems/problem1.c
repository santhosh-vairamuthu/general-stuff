// Given an array of numbers and a number k. Print the maximum possible k
// digit number which can be formed using given numbers.

// INPUT:
// Enter the array size: 4
// Enter the elements: 1 4 973 97
// Enter number of digits: 3

// OUTPUT: 974

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int max = 0;
int size_max;


void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int findSize(int k){
    int count = 0;
    while(k){
        count++;
        k/=10;
    }
    return count;
}
void printArray(int arr[], int n) {
    int size = findSize(arr[0]);
    int sum = arr[0];
    for(int i=1;i<n;i++){
        if(findSize(sum) >= size_max){
            break;
        }else{
            sum*=pow(10, findSize(arr[i]));
            sum+=arr[i];
            size=findSize(sum);
        }
    }
    if(size == size_max && sum>max){
        max = sum;
    }
}

void generateCombinations(int arr[], int data[], int start, int end, int index, int r) {
    if (index == r) {
        // Permutate each combination
        do {
            printArray(data, r);
        } while (next_permutation(data, data + r));

        return;
    }

    for (int i = start; i <= end && end - i + 1 >= r - index; i++) {
        data[index] = arr[i];
        generateCombinations(arr, data, i + 1, end, index + 1, r);
    }
}

int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int next_permutation(int *first, int *last) {
    if (first == last) return 0;
    int *i = last;
    if (first == --i) return 0;

    while (1) {
        int *i1, *i2;

        i1 = i;
        if (*--i < *i1) {
            i2 = last;
            while (!(*i < *--i2))
                /* pass */;
            swap(i, i2);
            reverse(i1, last);
            return 1;
        }

        if (i == first) {
            reverse(first, last);
            return 0;
        }
    }
}

void reverse(int *first, int *last) {
    while ((first != last) && (first != --last)) {
        swap(first++, last);
    }
}

int main() {
    
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d ",&arr[i]);
    }
    scanf("%d",&size_max);
    int data[n];
    for (int r = 1; r <= n; r++) {
        generateCombinations(arr, data, 0, n - 1, 0, r);
    }
    printf("%d",max);

    return 0;
}
