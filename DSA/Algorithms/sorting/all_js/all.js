class Sorting{
  static selectionSort (arr) {
    for (let i=0; i<arr.length; i++){
      let mini = i;

      // finding the lowest
      for (let j=i+1; j<arr.length; j++){
        if (arr[j]<arr[mini]){
          mini = j;
        }
      }

      // swapping with the lowest
      let temp = arr[i];
      arr[i] = arr[mini];
      arr[mini] = temp;
      
    }
    console.log(arr);
  }

  static bubbleSort(arr){
    for (let i=0; i<arr.length; i++){
      for (let j=i; j<arr.length; j++){
        if (arr[j]<arr[i]){
          let temp = arr[j];
          arr[j] = arr[i];
          arr[i] = temp;
        }
      }
    }
    console.log(arr)
  }

  static #partition(arr, lb, ub){
    let pivot = arr[lb];
    let start = lb;
    let end = ub;
    while (start<end){
      while (arr[start]<=pivot){
        start++;
      }
      while(arr[end]>pivot){
        end--;
      }
      if (start<end){
        let temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
      }
    }
    let temp = arr[end];
    arr[end] = arr[lb];
    arr[lb] = temp;
    return end;
  } 
  
  static quickSort(arr, lb, ub){
    if (lb < ub){
      let loc = this.#partition(arr, lb, ub);
      Sorting.quickSort(arr, lb, loc-1);
      Sorting.quickSort(arr, loc+1, ub);
    }
  }

  static insertionSort(arr){
    for (let i=1; i<arr.length; i++){
      let hole = i;
      let temp = arr[i];
      while(hole > 0 && temp<arr[hole-1]){
        arr[hole] = arr[hole-1];
        hole--;
      }
      arr[hole] = temp;
    }
    console.log(arr)
  }

  static mergeSort(arr){
    let len = arr.length;
    if (len<2){
      return;
    }

    let mid = Math.floor(len/2);
    let left = arr.slice(0, mid);
    let right = arr.slice(mid);

    Sorting.mergeSort(left);
    Sorting.mergeSort(right);

    let i,j,k;
    i=j=k=0;
    while (i<left.length && j<right.length){
      if (left[i]<right[j]){
        arr[k] = left[i];
        i++;
      }else{
        arr[k] = right[j];
        j++;
      }

      k++;
    }

    while (i<left.length){
      arr[k] = left[i];
      i++;
      k++;
    }
    
    while (j<right.length){
      arr[k] = right[j];
      j++;
      k++;
    }
  }
  
}

let arr = [5,4,3,2,1]
// Sorting.selectionSort(arr);
// Sorting.bubbleSort(arr);
// Sorting.quickSort(arr, 0, arr.length-1);
// console.log(arr);
// Sorting.insertionSort(arr)
Sorting.mergeSort(arr)
console.log(arr)