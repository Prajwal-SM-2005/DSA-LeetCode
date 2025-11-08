#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 10000

// Define a hash node structure
typedef struct Node {
    int key;        // the number (nums[i])
    int value;      // the index (i)
    struct Node* next;
} Node;

// Simple hash function (handles negatives too)
int hash(int key) {
    return abs(key) % TABLE_SIZE;
}

// Insert key-value pair into hash map
void insert(Node** table, int key, int value) {
    int index = hash(key);
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->key = key;
    newNode->value = value;
    newNode->next = table[index];
    table[index] = newNode;
}

// Search for a key in the hash map
int search(Node** table, int key) {
    int index = hash(key);
    Node* temp = table[index];
    while (temp) {
        if (temp->key == key)
            return temp->value;
        temp = temp->next;
    }
    return -1;  // not found
}

// Free hash map memory
void freeTable(Node** table) {
    for (int i = 0; i < TABLE_SIZE; i++) {
        Node* temp = table[i];
        while (temp) {
            Node* toDelete = temp;
            temp = temp->next;
            free(toDelete);
        }
    }
}

/**
 * LeetCode function definition
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    Node* table[TABLE_SIZE] = {NULL};  // initialize hash table

    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;

    for (int i = 0; i < numsSize; i++) {
        int complement = target - nums[i];
        int foundIndex = search(table, complement);

        if (foundIndex != -1) {
            result[0] = foundIndex;
            result[1] = i;
            freeTable(table);
            return result;
        }
        insert(table, nums[i], i);
    }

    *returnSize = 0;
    free(result);
    freeTable(table);
    return NULL;
}
