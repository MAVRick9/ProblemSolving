package greedy;
import java.util.*;
public class ADivdeB {
    public static void main(String[] args) {
        int a,b;
        double answer;
        Scanner sc=new Scanner(System.in);
        a=sc.nextInt();
        while(true) {
            b = sc.nextInt();
            if(b!=0)
                break;
        }
        answer=(double)a/b;
        System.out.println(answer);
    }
}
