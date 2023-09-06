package greedy;
import java.util.*;

public class Verifiable {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int []arr=new int[5];
        int v=0;
        for(int i=0;i<5;i++){
            arr[i]=sc.nextInt();
        }
        sc.close();
        for(int i=0;i<5;i++){
            v=v+arr[i]*arr[i];
        }

        System.out.println(v%10);
    }
}
