#include<stdio.h>
#include<stdlib.h>
#define N 5

struct Node{
	int val;
	struct Node *prev;
	struct Node *next;
};

struct Node *newNode(int val, struct Node *prev, struct Node *next){
	struct Node *node = (struct Node*)malloc(sizeof(struct Node));
	node->val = val;
	node->prev = prev;
	node->next = next;
	return node;
}

struct Node* removeFromHead(struct Node *first){
	struct Node *tmp = first->next;
	first->next = NULL;
	return tmp; 
}

struct Node* addToTail(struct Node *last, struct Node *next){
	last->next = next;
	next->prev = last;
	return next;
}


int main(int argc, char* argv[]){
	int MPref[N][N] = {{0, 1, 2, 3, 4}, {2, 0, 1, 3, 4}, {0, 2, 1, 3, 4}, {2, 1, 0, 3, 4}, {0, 2, 1, 4, 3}};
	int WRank[N][N] = {{2, 3, 0, 1, 4}, {3, 2, 1, 0, 4}, {3, 2, 0, 1, 4}, {3, 2, 0, 1, 4}, {0, 1, 2, 3, 4}};
	int Next[N] = {0, 0, 0, 0, 0};
	int Current[N] = {-1, -1, -1, -1, -1};
	
	struct Node *first = NULL, *last = NULL;
	struct Node *nodes[N] = {};
	for (int i=0; i<N; i++){
		nodes[i] = newNode(i, NULL, NULL);
		if (i == 0) first = last = nodes[i];
		else last = addToTail(last, nodes[i]);
	}

	while (first != NULL && Next[first->val] < N){
		printf("M%d proposes to W%d.\n", first->val, MPref[first->val][Next[first->val]]);
		if (Current[MPref[first->val][Next[first->val]]] < 0){
			printf("She's single. So they become engaged.\n");
			Current[MPref[first->val][Next[first->val]]] = first->val;
			first = removeFromHead(first);
		}
		else {
			printf("He's the number %d in W%d's preferences list.\n", WRank[MPref[first->val][Next[first->val]]][first->val], MPref[first->val][Next[first->val]]);
			printf("Her current partner M%d is the number %d in her preferences list.\n", Current[MPref[first->val][Next[first->val]]], WRank[MPref[first->val][Next[first->val]]][Current[MPref[first->val][Next[first->val]]]]);
			if (WRank[MPref[first->val][Next[first->val]]][first->val] < WRank[MPref[first->val][Next[first->val]]][Current[MPref[first->val][Next[first->val]]]]){
				printf("She will change her current partner.\n");
				last = addToTail(last, nodes[Current[MPref[first->val][Next[first->val]]]]);
				Current[MPref[first->val][Next[first->val]]] = first->val;
				first = removeFromHead(first);
			}
			else{
				printf("She will prefer her current partner.\n");
			}
		}
		if (first != NULL) Next[first->val]++;
		printf("\n");
	}

	printf("The resulting Stable Matching:\n");
	for (int i=0; i<N; i++){
		printf("(M%d, W%d):\n", Current[i], i);
		free(nodes[i]);
	}
	
	printf("\nMen preferences:\n");
	for (int i=0; i<N; i++){
		printf("M%d: ( ", i);
		for (int j=0; j<N; j++) printf("W%d ", MPref[i][j]);
		printf(")\n");
	}

	int WPref[N][N] = {};
	for (int i=0; i<N; i++) for (int j=0; j<N; j++) WPref[i][WRank[i][j]] = j;
	printf("\nWomen preferences:\n");
	for (int i=0; i<N; i++){
		printf("W%d: ( ", i);
		for (int j=0; j<N; j++) printf("M%d ", WPref[i][j]);
		printf(")\n");
	}
	return 0;
}
