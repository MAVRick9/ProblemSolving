package greedy;
import java.util.*;
public class Max {
    public static void main(String[] args) {
        int []arr=new int[9];
        int temp=0;
        int flag=0;
        Scanner sc=new Scanner(System.in);
        for(int i=0;i<9;i++){
            arr[i]= sc.nextInt();
        }
        sc.close();
        for(int i=0;i<9;i++){
           if(arr[i]>temp) {
                temp=arr[i];
                flag=i;
           }
        }
        System.out.println(temp);
        System.out.println(flag+1);
    }
}


//    int maxValue = -1;	// 최댓값을 갖고있을 변수
//    int maxValueIndex;	// 최댓값의 위치를 갖고있을 변수
//    int num;			// 입력받는 변수
//for (int i = 0; i < 9; i++) {
//
//        cin >> num;		// 입력받기
//
//        // 이전값들 중 최댓값보다 현재 num값이 더 크다면 최댓값과 인덱스를 현재 i로를 갱신
//        if (num > maxValue) {
//        maxValue = num;
//        maxValueIndex = i;
//        }
//        }