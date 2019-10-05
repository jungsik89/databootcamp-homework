Sub Stocks():

    Dim tickername As String
    Dim LastRow As Long
    Dim openprice, closeprice, yearlychange As Double
    Dim volumetotal As Double
    Dim yearlypercentage As Double
    Dim j As Long
    Dim i As Double
    Dim sheet As Worksheet
   
    For Each sheet In Worksheets
        sheet.Range("J1").Value = "Ticker Name"
        sheet.Range("K1").Value = "Yearly Change"
        sheet.Range("L1").Value = "Percentage Change"
        sheet.Range("M1").Value = "Total Stock Volume"
        'sheet.Range("Q1").Value = "Ticker"
        'sheet.Range("P2").Value = "Greatest % Increase"
        'sheet.Range("P3").Value = "Greatest % Decrease"
        'sheet.Range("P4").Value = "Greatest Total Volume"
        'sheet.Range("R1").Value = "Value"
        
 
        LastRow = sheet.Cells(Rows.Count, 1).End(xlUp).Row
        j = 2
        c = 0
        openvalue = 0
        closeprice = 0
        yearlychange = 0
        yearlypercentage = 0
        volumetotal = 0
        openprice = sheet.Cells(2, 3).Value
        
        For i = 2 To LastRow
        'LastRow
       
                              If sheet.Cells(i + 1, 1).Value <> sheet.Cells(i, 1).Value Then
                        
                                                 tickername = sheet.Cells(i, 1).Value
                                                 volumetotal = volumetotal + sheet.Cells(i, 7).Value
                                                 
                                                 closeprice = sheet.Cells(i, 6).Value
                                                 yearlychange = closeprice - openprice
                                                 percentagechange = (closeprice - openprice) / openprice
                                                 
                                                                           
                                                 'print values
                                                 sheet.Cells(j, 10).Value = tickername
                                                 sheet.Cells(j, 11).Value = yearlychange
                                                 sheet.Cells(j, 12).Value = percentagechange
                                                 sheet.Cells(j, 13).Value = volumetotal
                                                 
                                             If (yearlychange > 0) Then
                                                 sheet.Range("K" & j).Interior.ColorIndex = 4
                                             ElseIf (yearlychange <= 0) Then
                                                 sheet.Range("K" & j).Interior.ColorIndex = 3
                                             End If
                                                         
                                                 j = j + 1
                                                 volumetotal = 0
                                                 yearlychange = 0
                                                 percentagechange = 0
                              Else
                                                 volumetotal = volumetotal + sheet.Cells(i, 7).Value
                              End If
        Next i
 
 
        sheet.Range("P2").Value = "Max % Growth"
        sheet.Range("P3").Value = "Max % Decline"
        sheet.Range("P4").Value = "Largest stock value"
        sheet.Range("R1").Value = "Ticker Value"
        sheet.Range("Q1").Value = "Ticker"
         
         '
        sheet.Range("R2").Value = WorksheetFunction.Max(sheet.Range("L2:L" & LastRow))
        sheet.Range("R3").Value = WorksheetFunction.Max(sheet.Range("L2:L" & LastRow))
        sheet.Range("R4").Value = WorksheetFunction.Max(sheet.Range("M2:M" & LastRow))
        
        Dim Increase, Decrease, largest As Double
        Increase = WorksheetFunction.Match(sheet.Range("L2").Value, sheet.Range("L2:L" & LastRow), 0) + 1
        Decrease = WorksheetFunction.Match(sheet.Range("L3").Value, sheet.Range("L2:L" & LastRow), 0) + 1
        largest = WorksheetFunction.Match(sheet.Range("M4").Value, sheet.Range("M2:M" & LastRow), 0) + 1
        
       
        sheet.Range("R2").Value = sheet.Range("I" & Increase).Value
        sheet.Range("R3").Value = sheet.Range("I" & Decrease).Value
        sheet.Range("R4").Value = sheet.Range("I" & largest).Value
        
    
    Next sheet
   
End Sub

Sub Clear()
Dim sheet As Worksheet

For Each sheet In Worksheets


    sheet.Range("J1:R19999").Clear

Next sheet

End Sub

