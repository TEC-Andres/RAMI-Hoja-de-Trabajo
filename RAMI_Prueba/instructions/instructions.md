# COMMANDS AVAILABLE
**Bold, italics, and underlining**
    - bold: \textbf{text} or select text and press **CTRL/COMMAND + B**;
    
    - italics: \textit{text} or select text and press **CTRL/COMMAND + I**;
    
    - underlining: \underline{text} or select text;

**\blankpage** 
    Insert a blank page;
    
**\boxedtext{text}**
    Surround the one-line text with a box;

**\pagebreak**
    Insert a page break;

**\insertlines{5}**
    Insert 5 drawn lines for the student's answer;
    
**\insertspace{5}**
    Insert 5 blank lines for the student's answer;

**\indent text**
    To add an indentation before text;
    
**To manually break the line**
    Insert the symbol \\ where you want to break the line;

**To insert tables**
   \begin{tabular}{ align1 align2 align3 } 
       cell1 & cell2 & cell3 \\ 
       cell4 & cell5 & cell6 \\ 
       cell7 & cell8 & cell9 \\ 
   \end{tabular}
   
   where **alignX** indicates the alignment of each column that could be:
      - c: center
      - l: left
      - r: right;

**To insert images**
  1. Upload an image on the left menu;
     
  2. Insert the command
     **\includegraphics[scale=size_percent]{image_file_name}**

  3. Examples: 
      - **\includegraphics[scale=1]{piaget}**   % to show 100% of the original size;
        
      - **\includegraphics[scale=0.5]{piaget}** % to show 50% of the original size;
        
      - **\includegraphics[scale=2.2]{piaget}** % to show 220% of the original size.
    
**Aligning a text or block**
  **center**:
      \begin{center}
          text
      \end{center}

  **left**:
      \begin{flushleft}
          text
      \end{flushleft}
      
  **right**:
      \begin{flushright}
          text
      \end{flushright}