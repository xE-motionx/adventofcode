//.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.
// Author: Frederik Brönner
// Date: 2023.12.05
// AOC: 03
// Problem description:
//   From a visual representation, fetch all marked numbers.
//.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.

// <-- imports -->
using System;
using System.IO;

public class d03p01
{
  // <-- functions -->

  static public void Main()
  {
    // <-- vars -->
    string dataSource = @"./example"; // "./example" "./input"
    string line;
    string[,] data = new string[0,0];
    int lineCount = 0;
    
    // <-- main -->
    StreamReader sr = new StreamReader(dataSource);
    line = sr.ReadLine();
    while (line != null){
      for(int i = 0; i < line.Length; i++){
        data[lineCount,i] = line[i].ToString();
      }
      line = sr.ReadLine();
      lineCount++;
    }
    sr.Close();
  }
}
