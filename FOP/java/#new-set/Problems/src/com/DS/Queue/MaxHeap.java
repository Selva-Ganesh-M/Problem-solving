package com.DS.Queue;
// import java.util.ArrayList;

public class MaxHeap {
    private int [] arr;
    private int maxSize;
    private int currSize;

    public MaxHeap(int size){
        this.arr = new int[size];
        this.maxSize = size;
        this.currSize = 0;
    }

    private int parent(int i){
        return (i!=0) ? (int)Math.floor((i-1)/2) : 0;
    }

    private int lc(int i){
        return (2*i)+1;
    }

    private int rc(int i){
        return (2*i)+2;
    }

    private void maxHeapify(int pos){
        if (pos<0) return;
        int leftChild = this.lc(pos);
        int rightChild = this.rc(pos);
        int greatest = pos;
        if (leftChild<maxSize && this.arr[leftChild] > this.arr[pos]){
            greatest = leftChild;
        }
        if (rightChild<maxSize && this.arr[rightChild] > this.arr[greatest]){
            greatest = rightChild;
        }
        if (greatest!=pos){
            arr[greatest] = arr[greatest] + arr[pos];
            arr[pos] = arr[greatest] - arr[pos];
            arr[greatest] = arr[greatest] - arr[pos];
            this.maxHeapify(parent(pos));
        }
    }

    // insert
    public void insertMax(int num){
            this.arr[currSize] = num;
            this.maxHeapify(this.parent(currSize));
            this.currSize++;
    }


    // poll
    public void poll(){
        if (this.currSize ==0 ){
            System.out.println("No items to poll.");
        }
        else {
            System.out.println(String.format("polled value is + %d", this.arr[0]));
            
            // return if only one item is present
            if (this.currSize==1) return;

            this.arr[0] = this.arr[-1];
            this.arr[-1] = 0;
            this.currSize--;

            this.maxHeapify(0);
        }
    }

    public void print(){
        for (int i: this.arr){
            System.out.print(i+ " ");
        }
        System.out.println();
    }

}
