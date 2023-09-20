class Search{
  static binarySearch(arr, src, start, end){
    if (start > end){
      return -1
    }
    let mid = Math.floor((start + end)/2);
    if (arr[mid] == src){
      return mid;
    }
    else if (src < arr[mid]){
      return Search.binarySearch(arr, src, start, mid-1);
    }else if(src > arr[mid]){
      return Search.binarySearch(arr, src, mid+1, end);
    }
  }
}

let arr = [1,2,3,4];
console.log(Search.binarySearch(arr, 5, 0, arr.length-1))