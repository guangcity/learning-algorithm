//
// Created by Qian Hu on 2018/12/5.
//

#include <stdio.h>
#include <stdlib.h>


typedef struct TreeNode {
    struct TreeNode* left;
    struct TreeNode* right;
    int value;
} TreeNode, *Tree;

typedef struct Stack {
    TreeNode *data;
    int top;
} Stack;


Tree buildTree(int pre[], int post[], int len) {
    Tree tree;
    if (!len) {
        return NULL;
    }
    tree = (Tree)malloc(sizeof(TreeNode));
    tree->value = pre[0];
    if (len == 1) {
        tree->left = NULL;
        tree->right = NULL;
        return tree;
    }
    int i;
    for (i = 0; i < len && post[i] != pre[1]; i++);
    tree->left = buildTree(pre + 1, post, i + 1);
    tree->right = buildTree(pre + i + 2, post + i + 1, len - i - 2);
    return tree;
}


void in_order_traverse_tree_recursion(Tree tree) {
    if (tree) {
        in_order_traverse_tree_recursion(tree->left);
        printf("%d ", tree->value);
        in_order_traverse_tree_recursion(tree->right);
    }
}


void in_order_traverse_tree_iteration(Tree tree, int num) {
    Stack *stack = (Stack *)malloc(sizeof(stack));
    stack->data = (TreeNode *)malloc(sizeof(TreeNode) * num);
    int top = 0;

    TreeNode* p = tree;
    while (1) {
        while (p) {
            stack->data[top++] = *p;
            p = p->left;
        }
        if (top == 0) {
            break;
        }
        p = &stack->data[--top];
        printf("%d ", p->value);
        p = p->right;
    }
}


int main() {
    int num;
    Tree tree;
    scanf("%d", &num);
    int *pre_order, *post_order;
    pre_order = (int*)malloc(sizeof(int) * num);
    post_order = (int*)malloc(sizeof(int) * num);
    for (int i = 0; i < num; i++) {
        scanf("%d", &pre_order[i]);
    }
    for (int i = 0; i < num; i++) {
        scanf("%d", &post_order[i]);
    }
    tree = buildTree(pre_order, post_order, num);
//    in_order_traverse_tree_recursion(tree);
    in_order_traverse_tree_iteration(tree, num);
    return 0;
}