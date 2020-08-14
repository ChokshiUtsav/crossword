import java.text.*;
import java.util.*;

public class Language{
    public static void main(String[] args) {
        String text = "વાનર";
        Locale gujarati = new Locale("gu","IN");
        System.out.println(gujarati.getUnicodeLocaleKeys().size());
        for(String s : gujarati.getUnicodeLocaleKeys()){
            System.out.println(s);
        }
        BreakIterator breaker = BreakIterator.getCharacterInstance(gujarati);
        breaker.setText(text);
        int start = breaker.first();
        for (int end = breaker.next(); end != BreakIterator.DONE; start = end, end = breaker.next()) {
            System.out.println(text.substring(start,end));
        }    
    }
}