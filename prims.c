
#include<stdio.h>
#include <limits.h> 
#include <stdbool.h> 
#define infinity 9999
#define max 5


void primMST(int [max][max]);
int minkey(int [max],bool [max]);
void primMST(int [max][max]);
void main(int argc, char const *argv[])
{


int graph[max][max] = { { 0, 2, 0, 6, 0 }, 
                        { 2, 0, 3, 8, 5 }, 
                        { 0, 3, 0, 0, 7 }, 
                        { 6, 8, 0, 0, 9 }, 
                        { 0, 5, 7, 9, 0 } }; 
  
    // give the entire graph to function primMST
    primMST(graph);
    

    
}



void primMST(int graph[max][max]){

    int parent[max],key[max],i,v;  
    bool mstSet[max];

    //now initialize the parent array elements to null and key array to infinite

    for(i=0;i<max;i++){

        parent[i] = NULL;
        key[i] = infinity ;
        mstSet[i] = false;

    } 

    key[0] = 0;                         // this will pick node 0 as the starting node
    parent[0] = -1 ;                // starting node will have no parent

    for(i=0;i<max;i++){
        int u = minkey(key,mstSet);

        mstSet[u] = true ;         // because it has now been visited

        for(v=0;v<max;v++){

            if(graph[u][v] && graph[u][v] < key[v]){

                key[v] = graph[u][v] ;
                parent[v] = u ;

            }

        }

    }

    printMST(parent, graph);

}

int minkey(int key[max], bool mstSet[]){

    int min = infinity,i,min_index ;

    for(i=0;i<max;i++){

        if(key[i] < min && mstSet[i] == false){
            min = key[i];
            min_index = i ;
        }
    }

    return min_index ;

}

 void printMST(int parent[max], int graph[max][max]){

     
     printf("Edge \tWeight\n"); 
    for (int i = 0; i < max; i++) 
        printf("%d - %d \t%d \n", parent[i], i, graph[i][parent[i]]);
 }