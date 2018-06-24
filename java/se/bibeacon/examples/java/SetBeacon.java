package se.bibeacon.examples.java;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.URL;
import java.net.URLConnection;

public class SetBeacon {

   public static boolean setColor( String systemid, String color ) {
      try {
         URLConnection connection = new URL("https://api.cilamp.se/v1/" + systemid).openConnection();
         connection.setDoOutput(true);
         connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
         OutputStream output = connection.getOutputStream();
         output.write(("color=" + color).getBytes());
         InputStream response = connection.getInputStream();
      } catch( Exception e ) {
         System.err.println( e );
         return false;
      }
      return true;
   }

   // Usage: <systemid> <color>
   public static void main(String args[]) {
      setColor(args[0], args[1]);
   }
}
