package greedy;
import java.util.*;
public class MostUsedAlpha {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        int[] arr=new int[26];
        int max=-1; //0일수도 있으니
        char c='?';

        sc.close();

        for(int i=0;i<s.length();i++){
            if(65<=s.charAt(i)&&s.charAt(i)<=90){
                arr[s.charAt(i)-65]++;
            }
            else {
                arr[s.charAt(i)-97]++;
            }
        }

        for (int i=0;i<arr.length;i++){
            if(arr[i]>max){
                max=arr[i];
                c=(char)(i+65);
            } else if (arr[i]==max) {
                c='?';
            }
        }

        System.out.println(c);

    }
}
