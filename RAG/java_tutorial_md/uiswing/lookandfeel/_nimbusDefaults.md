[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Modifying the Look and Feel

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Modifying the Look and Feel](index.html)

[« Previous](color.html) • [TOC](../TOC.html)

# Nimbus Defaults

All of the Nimbus properties are stored as keys in the
`UIManager`'s defaults table. You can retrieve
and modify any of these values to customize the look and feel
of your application.
This page lists all of the Nimbus defaults and was originally posted on
Jasper Potts' blog,
[Caffeine Induced Ramblings](http://www.jasperpotts.com/blog/2008/08/nimbus-uimanager-uidefaults/). He has also posted the code to generate this page,
[NimbusBrowser.java](http://jasperpotts.com/blogfiles/nimbusdefaults/NimbusBrowser.java).

### Primary Colors

| Key | Value | Preview |
| --- | --- | --- |
| `control` | ``` #d6d9df (214,217,223) ``` |  |
| `info` | ``` #f2f2bd (242,242,189) ``` |  |
| `nimbusAlertYellow` | ``` #ffdc23 (255,220,35) ``` |  |
| `nimbusBase` | ``` #33628c (51,98,140) ``` |  |
| `nimbusDisabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `nimbusFocus` | ``` #73a4d1 (115,164,209) ``` |  |
| `nimbusGreen` | ``` #b0b332 (176,179,50) ``` |  |
| `nimbusInfoBlue` | ``` #2f5cb4 (47,92,180) ``` |  |
| `nimbusLightBackground` | ``` #ffffff (255,255,255) ``` |  |
| `nimbusOrange` | ``` #bf6204 (191,98,4) ``` |  |
| `nimbusRed` | ``` #a92e22 (169,46,34) ``` |  |
| `nimbusSelectedText` | ``` #ffffff (255,255,255) ``` |  |
| `nimbusSelectionBackground` | ``` #39698a (57,105,138) ``` |  |
| `text` | ``` #000000 (0,0,0) ``` |  |

### Secondary Colors

| Key | Value | Preview |
| --- | --- | --- |
| `activeCaption` | ``` #babec6 (186,190,198) ``` |  |
| `background` | ``` #d6d9df (214,217,223) ``` |  |
| `controlDkShadow` | ``` #a4abb8 (164,171,184) ``` |  |
| `controlHighlight` | ``` #e9ecf2 (233,236,242) ``` |  |
| `controlLHighlight` | ``` #f7f8fa (247,248,250) ``` |  |
| `controlShadow` | ``` #ccd3e0 (204,211,224) ``` |  |
| `controlText` | ``` #000000 (0,0,0) ``` |  |
| `desktop` | ``` #3d6079 (61,96,121) ``` |  |
| `inactiveCaption` | ``` #bdc1c8 (189,193,200) ``` |  |
| `infoText` | ``` #000000 (0,0,0) ``` |  |
| `menu` | ``` #edeff2 (237,239,242) ``` |  |
| `menuText` | ``` #000000 (0,0,0) ``` |  |
| `nimbusBlueGrey` | ``` #a9b0be (169,176,190) ``` |  |
| `nimbusBorder` | ``` #9297a1 (146,151,161) ``` |  |
| `nimbusSelection` | ``` #39698a (57,105,138) ``` |  |
| `scrollbar` | ``` #cdd0d5 (205,208,213) ``` |  |
| `textBackground` | ``` #39698a (57,105,138) ``` |  |
| `textForeground` | ``` #000000 (0,0,0) ``` |  |
| `textHighlight` | ``` #39698a (57,105,138) ``` |  |
| `textHighlightText` | ``` #ffffff (255,255,255) ``` |  |
| `textInactiveText` | ``` #8e8f91 (142,143,145) ``` |  |

### Components

#### DesktopIcon

| Key | Value | Preview |
| --- | --- | --- |
| `DesktopIcon.background` | ``` #d6d9df (214,217,223) ``` |  |
| `DesktopIcon.contentMargins` | Insets (4,6,5,4) |  |
| `DesktopIcon.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `DesktopIcon.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `DesktopIcon.font` | Font "SansSerif 12 |  |
| `DesktopIcon.foreground` | ``` #000000 (0,0,0) ``` |  |
| `DesktopIcon[Enabled].backgroundPainter` | Painter |  |

#### FileChooser

| Key | Value | Preview |
| --- | --- | --- |
| `FileChooser.ancestorInputMap` |  |  |
| `FileChooser.background` | ``` #d6d9df (214,217,223) ``` |  |
| `FileChooser.contentMargins` | Insets (10,10,10,10) |  |
| `FileChooser.detailsViewIcon` | Icon 16 x 16 |  |
| `FileChooser.directoryIcon` | Icon 16 x 16 |  |
| `FileChooser.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `FileChooser.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `FileChooser.fileIcon` | Icon 16 x 16 |  |
| `FileChooser.floppyDriveIcon` | Icon 16 x 16 |  |
| `FileChooser.font` | Font "SansSerif 12 |  |
| `FileChooser.foreground` | ``` #000000 (0,0,0) ``` |  |
| `FileChooser.hardDriveIcon` | Icon 16 x 16 |  |
| `FileChooser.homeFolderIcon` | Icon 16 x 16 |  |
| `FileChooser.listViewIcon` | Icon 16 x 16 |  |
| `FileChooser.newFolderIcon` | Icon 16 x 16 |  |
| `FileChooser.opaque` | true |  |
| `FileChooser.upFolderIcon` | Icon 16 x 16 |  |
| `FileChooser.usesSingleFilePane` | true |  |
| `FileChooser[Enabled].backgroundPainter` | Painter |  |
| `FileChooser[Enabled].detailsViewIconPainter` | Painter |  |
| `FileChooser[Enabled].directoryIconPainter` | Painter |  |
| `FileChooser[Enabled].fileIconPainter` | Painter |  |
| `FileChooser[Enabled].floppyDriveIconPainter` | Painter |  |
| `FileChooser[Enabled].hardDriveIconPainter` | Painter |  |
| `FileChooser[Enabled].homeFolderIconPainter` | Painter |  |
| `FileChooser[Enabled].listViewIconPainter` | Painter |  |
| `FileChooser[Enabled].newFolderIconPainter` | Painter |  |
| `FileChooser[Enabled].upFolderIconPainter` | Painter |  |

#### RootPane

| Key | Value | Preview |
| --- | --- | --- |
| `RootPane.background` | ``` #d6d9df (214,217,223) ``` |  |
| `RootPane.contentMargins` | Insets (0,0,0,0) |  |
| `RootPane.defaultButtonWindowKeyBindings` | [Ljava.lang.Object;@2092dcdb |  |
| `RootPane.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `RootPane.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `RootPane.font` | Font "SansSerif 12 |  |
| `RootPane.foreground` | ``` #000000 (0,0,0) ``` |  |
| `RootPane.opaque` | true |  |

#### TextPane

| Key | Value | Preview |
| --- | --- | --- |
| `TextPane.background` | ``` #d6d9df (214,217,223) ``` |  |
| `TextPane.contentMargins` | Insets (4,6,4,6) |  |
| `TextPane.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `TextPane.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `TextPane.focusInputMap` |  |  |
| `TextPane.font` | Font "SansSerif 12 |  |
| `TextPane.foreground` | ``` #000000 (0,0,0) ``` |  |
| `TextPane.opaque` | true |  |
| `TextPane[Disabled].backgroundPainter` | Painter |  |
| `TextPane[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `TextPane[Enabled].backgroundPainter` | Painter |  |
| `TextPane[Selected].backgroundPainter` | Painter |  |
| `TextPane[Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |

#### FormattedTextField

| Key | Value | Preview |
| --- | --- | --- |
| `FormattedTextField.background` | ``` #d6d9df (214,217,223) ``` |  |
| `FormattedTextField.contentMargins` | Insets (6,6,6,6) |  |
| `FormattedTextField.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `FormattedTextField.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `FormattedTextField.focusInputMap` |  |  |
| `FormattedTextField.font` | Font "SansSerif 12 |  |
| `FormattedTextField.foreground` | ``` #000000 (0,0,0) ``` |  |
| `FormattedTextField[Disabled].backgroundPainter` | Painter |  |
| `FormattedTextField[Disabled].borderPainter` | Painter |  |
| `FormattedTextField[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `FormattedTextField[Enabled].backgroundPainter` | Painter |  |
| `FormattedTextField[Enabled].borderPainter` | Painter |  |
| `FormattedTextField[Focused].borderPainter` | Painter |  |
| `FormattedTextField[Selected].backgroundPainter` | Painter |  |
| `FormattedTextField[Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |

#### Spinner

| Key | Value | Preview |
| --- | --- | --- |
| `Spinner.ancestorInputMap` |  |  |
| `Spinner.background` | ``` #d6d9df (214,217,223) ``` |  |
| `Spinner.contentMargins` | Insets (0,0,0,0) |  |
| `Spinner.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `Spinner.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `Spinner.font` | Font "SansSerif 12 |  |
| `Spinner.foreground` | ``` #000000 (0,0,0) ``` |  |
| `Spinner:"Spinner.editor".contentMargins` | Insets (0,0,0,0) |  |
| `Spinner:"Spinner.nextButton".contentMargins` | Insets (0,0,0,0) |  |
| `Spinner:"Spinner.nextButton".size` | 20 |  |
| `Spinner:"Spinner.nextButton"[Disabled].backgroundPainter` | Painter |  |
| `Spinner:"Spinner.nextButton"[Disabled].foregroundPainter` | Painter |  |
| `Spinner:"Spinner.nextButton"[Enabled].backgroundPainter` | Painter |  |
| `Spinner:"Spinner.nextButton"[Enabled].foregroundPainter` | Painter |  |
| `Spinner:"Spinner.nextButton"[Focused+MouseOver].backgroundPainter` | Painter |  |
| `Spinner:"Spinner.nextButton"[Focused+MouseOver].foregroundPainter` | Painter |  |
| `Spinner:"Spinner.nextButton"[Focused+Pressed].backgroundPainter` | Painter |  |
| `Spinner:"Spinner.nextButton"[Focused+Pressed].foregroundPainter` | Painter |  |
| `Spinner:"Spinner.nextButton"[Focused].backgroundPainter` | Painter |  |
| `Spinner:"Spinner.nextButton"[Focused].foregroundPainter` | Painter |  |
| `Spinner:"Spinner.nextButton"[MouseOver].backgroundPainter` | Painter |  |
| `Spinner:"Spinner.nextButton"[MouseOver].foregroundPainter` | Painter |  |
| `Spinner:"Spinner.nextButton"[Pressed].backgroundPainter` | Painter |  |
| `Spinner:"Spinner.nextButton"[Pressed].foregroundPainter` | Painter |  |
| `Spinner:"Spinner.previousButton".contentMargins` | Insets (0,0,0,0) |  |
| `Spinner:"Spinner.previousButton".size` | 20 |  |
| `Spinner:"Spinner.previousButton"[Disabled].backgroundPainter` | Painter |  |
| `Spinner:"Spinner.previousButton"[Disabled].foregroundPainter` | Painter |  |
| `Spinner:"Spinner.previousButton"[Enabled].backgroundPainter` | Painter |  |
| `Spinner:"Spinner.previousButton"[Enabled].foregroundPainter` | Painter |  |
| `Spinner:"Spinner.previousButton"[Focused+MouseOver].backgroundPainter` | Painter |  |
| `Spinner:"Spinner.previousButton"[Focused+MouseOver].foregroundPainter` | Painter |  |
| `Spinner:"Spinner.previousButton"[Focused+Pressed].backgroundPainter` | Painter |  |
| `Spinner:"Spinner.previousButton"[Focused+Pressed].foregroundPainter` | Painter |  |
| `Spinner:"Spinner.previousButton"[Focused].backgroundPainter` | Painter |  |
| `Spinner:"Spinner.previousButton"[Focused].foregroundPainter` | Painter |  |
| `Spinner:"Spinner.previousButton"[MouseOver].backgroundPainter` | Painter |  |
| `Spinner:"Spinner.previousButton"[MouseOver].foregroundPainter` | Painter |  |
| `Spinner:"Spinner.previousButton"[Pressed].backgroundPainter` | Painter |  |
| `Spinner:"Spinner.previousButton"[Pressed].foregroundPainter` | Painter |  |
| `Spinner:Panel:"Spinner.formattedTextField".contentMargins` | Insets (6,6,5,6) |  |
| `Spinner:Panel:"Spinner.formattedTextField"[Disabled].backgroundPainter` | Painter |  |
| `Spinner:Panel:"Spinner.formattedTextField"[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `Spinner:Panel:"Spinner.formattedTextField"[Enabled].backgroundPainter` | Painter |  |
| `Spinner:Panel:"Spinner.formattedTextField"[Focused+Selected].backgroundPainter` | Painter |  |
| `Spinner:Panel:"Spinner.formattedTextField"[Focused+Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `Spinner:Panel:"Spinner.formattedTextField"[Focused].backgroundPainter` | Painter |  |
| `Spinner:Panel:"Spinner.formattedTextField"[Selected].backgroundPainter` | Painter |  |
| `Spinner:Panel:"Spinner.formattedTextField"[Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |

#### PopupMenuSeparator

| Key | Value | Preview |
| --- | --- | --- |
| `PopupMenuSeparator.background` | ``` #d6d9df (214,217,223) ``` |  |
| `PopupMenuSeparator.contentMargins` | Insets (1,0,2,0) |  |
| `PopupMenuSeparator.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `PopupMenuSeparator.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `PopupMenuSeparator.font` | Font "SansSerif 12 |  |
| `PopupMenuSeparator.foreground` | ``` #000000 (0,0,0) ``` |  |
| `PopupMenuSeparator[Enabled].backgroundPainter` | Painter |  |

#### Table

| Key | Value | Preview |
| --- | --- | --- |
| `Table.alternateRowColor` | ``` #f2f2f2 (242,242,242) ``` |  |
| `Table.ancestorInputMap` |  |  |
| `Table.ancestorInputMap.RightToLeft` |  |  |
| `Table.ascendingSortIcon` | Icon 7 x 7 |  |
| `Table.background` | ``` #ffffff (255,255,255) ``` |  |
| `Table.cellNoFocusBorder` | Border Insets(2,5,2,5) |  |
| `Table.contentMargins` | Insets (0,0,0,0) |  |
| `Table.descendingSortIcon` | Icon 7 x 7 |  |
| `Table.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `Table.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `Table.dropLineColor` | ``` #73a4d1 (115,164,209) ``` |  |
| `Table.dropLineShortColor` | ``` #bf6204 (191,98,4) ``` |  |
| `Table.focusCellHighlightBorder` | Border Insets(2,5,2,5) |  |
| `Table.font` | Font "SansSerif 12 |  |
| `Table.foreground` | ``` #000000 (0,0,0) ``` |  |
| `Table.intercellSpacing` | Dimension (0,0) |  |
| `Table.opaque` | true |  |
| `Table.rendererUseTableColors` | true |  |
| `Table.rendererUseUIBorder` | true |  |
| `Table.scrollPaneCornerComponent` | class com.sun.java.swing.plaf.nimbus.TableScrollPaneCorner |  |
| `Table.showGrid` | false |  |
| `Table.textForeground` | ``` #232324 (35,35,36) ``` |  |
| `Table:"Table.cellRenderer".background` | ``` #ffffff (255,255,255) ``` |  |
| `Table:"Table.cellRenderer".contentMargins` | Insets (0,0,0,0) |  |
| `Table:"Table.cellRenderer".opaque` | true |  |
| `Table[Disabled+Selected].textBackground` | ``` #39698a (57,105,138) ``` |  |
| `Table[Enabled+Selected].textBackground` | ``` #39698a (57,105,138) ``` |  |
| `Table[Enabled+Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |

#### TextArea

| Key | Value | Preview |
| --- | --- | --- |
| `TextArea.NotInScrollPane` | NotInScrollPane |  |
| `TextArea.States` | Enabled,MouseOver,Pressed,Selected,Disabled,Focused,NotInScrollPane |  |
| `TextArea.background` | ``` #d6d9df (214,217,223) ``` |  |
| `TextArea.contentMargins` | Insets (6,6,6,6) |  |
| `TextArea.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `TextArea.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `TextArea.focusInputMap` |  |  |
| `TextArea.font` | Font "SansSerif 12 |  |
| `TextArea.foreground` | ``` #000000 (0,0,0) ``` |  |
| `TextArea[Disabled+NotInScrollPane].backgroundPainter` | Painter |  |
| `TextArea[Disabled+NotInScrollPane].borderPainter` | Painter |  |
| `TextArea[Disabled+NotInScrollPane].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `TextArea[Disabled].backgroundPainter` | Painter |  |
| `TextArea[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `TextArea[Enabled+NotInScrollPane].backgroundPainter` | Painter |  |
| `TextArea[Enabled+NotInScrollPane].borderPainter` | Painter |  |
| `TextArea[Enabled].backgroundPainter` | Painter |  |
| `TextArea[Focused+NotInScrollPane].borderPainter` | Painter |  |
| `TextArea[Selected].backgroundPainter` | Painter |  |
| `TextArea[Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |

#### Slider

| Key | Value | Preview |
| --- | --- | --- |
| `Slider.ArrowShape` | ArrowShape |  |
| `Slider.States` | Enabled,MouseOver,Pressed,Disabled,Focused,Selected,ArrowShape |  |
| `Slider.background` | ``` #d6d9df (214,217,223) ``` |  |
| `Slider.contentMargins` | Insets (0,0,0,0) |  |
| `Slider.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `Slider.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `Slider.focusInputMap` |  |  |
| `Slider.focusInputMap.RightToLeft` |  |  |
| `Slider.font` | Font "SansSerif 12 |  |
| `Slider.foreground` | ``` #000000 (0,0,0) ``` |  |
| `Slider.paintValue` | false |  |
| `Slider.thumbHeight` | 17 |  |
| `Slider.thumbWidth` | 17 |  |
| `Slider.tickColor` | ``` #232830 (35,40,48) ``` |  |
| `Slider.trackBorder` | 0 |  |
| `Slider:SliderThumb.ArrowShape` | ArrowShape |  |
| `Slider:SliderThumb.States` | Enabled,MouseOver,Pressed,Disabled,Focused,Selected,ArrowShape |  |
| `Slider:SliderThumb.contentMargins` | Insets (0,0,0,0) |  |
| `Slider:SliderThumb[ArrowShape+Disabled].backgroundPainter` | Painter |  |
| `Slider:SliderThumb[ArrowShape+Enabled].backgroundPainter` | Painter |  |
| `Slider:SliderThumb[ArrowShape+Focused+MouseOver].backgroundPainter` | Painter |  |
| `Slider:SliderThumb[ArrowShape+Focused+Pressed].backgroundPainter` | Painter |  |
| `Slider:SliderThumb[ArrowShape+Focused].backgroundPainter` | Painter |  |
| `Slider:SliderThumb[ArrowShape+MouseOver].backgroundPainter` | Painter |  |
| `Slider:SliderThumb[ArrowShape+Pressed].backgroundPainter` | Painter |  |
| `Slider:SliderThumb[Disabled].backgroundPainter` | Painter |  |
| `Slider:SliderThumb[Enabled].backgroundPainter` | Painter |  |
| `Slider:SliderThumb[Focused+MouseOver].backgroundPainter` | Painter |  |
| `Slider:SliderThumb[Focused+Pressed].backgroundPainter` | Painter |  |
| `Slider:SliderThumb[Focused].backgroundPainter` | Painter |  |
| `Slider:SliderThumb[MouseOver].backgroundPainter` | Painter |  |
| `Slider:SliderThumb[Pressed].backgroundPainter` | Painter |  |
| `Slider:SliderTrack.ArrowShape` | ArrowShape |  |
| `Slider:SliderTrack.States` | Enabled,MouseOver,Pressed,Disabled,Focused,Selected,ArrowShape |  |
| `Slider:SliderTrack.contentMargins` | Insets (0,0,0,0) |  |
| `Slider:SliderTrack[Disabled].backgroundPainter` | Painter |  |
| `Slider:SliderTrack[Enabled].backgroundPainter` | Painter |  |

#### InternalFrameTitlePane

| Key | Value | Preview |
| --- | --- | --- |
| `InternalFrameTitlePane.background` | ``` #d6d9df (214,217,223) ``` |  |
| `InternalFrameTitlePane.contentMargins` | Insets (0,0,0,0) |  |
| `InternalFrameTitlePane.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `InternalFrameTitlePane.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `InternalFrameTitlePane.font` | Font "SansSerif 12 |  |
| `InternalFrameTitlePane.foreground` | ``` #000000 (0,0,0) ``` |  |
| `InternalFrameTitlePane.maxFrameIconSize` | Dimension (18,18) |  |

#### ColorChooser

| Key | Value | Preview |
| --- | --- | --- |
| `ColorChooser.background` | ``` #d6d9df (214,217,223) ``` |  |
| `ColorChooser.contentMargins` | Insets (5,0,0,0) |  |
| `ColorChooser.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `ColorChooser.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `ColorChooser.font` | Font "SansSerif 12 |  |
| `ColorChooser.foreground` | ``` #000000 (0,0,0) ``` |  |
| `ColorChooser.swatchesDefaultRecentColor` | ``` #ffffff (255,255,255) ``` |  |
| `ColorChooser.swatchesRecentSwatchSize` | Dimension (10,10) |  |
| `ColorChooser.swatchesSwatchSize` | Dimension (10,10) |  |
| `ColorChooser:"ColorChooser.previewPanelHolder".contentMargins` | Insets (0,5,10,5) |  |
| `ColorChooser:"ColorChooser.previewPanelHolder":"OptionPane.label".contentMargins` | Insets (0,10,10,10) |  |

#### DesktopPane

| Key | Value | Preview |
| --- | --- | --- |
| `DesktopPane.background` | ``` #d6d9df (214,217,223) ``` |  |
| `DesktopPane.contentMargins` | Insets (0,0,0,0) |  |
| `DesktopPane.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `DesktopPane.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `DesktopPane.font` | Font "SansSerif 12 |  |
| `DesktopPane.foreground` | ``` #000000 (0,0,0) ``` |  |
| `DesktopPane.opaque` | true |  |
| `DesktopPane[Enabled].backgroundPainter` | Painter |  |

#### Menu

| Key | Value | Preview |
| --- | --- | --- |
| `Menu.arrowIcon` | Icon 9 x 10 |  |
| `Menu.background` | ``` #d6d9df (214,217,223) ``` |  |
| `Menu.contentMargins` | Insets (1,12,2,5) |  |
| `Menu.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `Menu.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `Menu.font` | Font "SansSerif 12 |  |
| `Menu.foreground` | ``` #232324 (35,35,36) ``` |  |
| `Menu:MenuItemAccelerator.contentMargins` | Insets (0,0,0,0) |  |
| `Menu:MenuItemAccelerator[MouseOver].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `Menu[Disabled].arrowIconPainter` | Painter |  |
| `Menu[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `Menu[Enabled+Selected].arrowIconPainter` | Painter |  |
| `Menu[Enabled+Selected].backgroundPainter` | Painter |  |
| `Menu[Enabled+Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `Menu[Enabled].arrowIconPainter` | Painter |  |
| `Menu[Enabled].textForeground` | ``` #232324 (35,35,36) ``` |  |

#### PasswordField

| Key | Value | Preview |
| --- | --- | --- |
| `PasswordField.background` | ``` #d6d9df (214,217,223) ``` |  |
| `PasswordField.contentMargins` | Insets (6,6,6,6) |  |
| `PasswordField.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `PasswordField.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `PasswordField.focusInputMap` |  |  |
| `PasswordField.font` | Font "SansSerif 12 |  |
| `PasswordField.foreground` | ``` #000000 (0,0,0) ``` |  |
| `PasswordField[Disabled].backgroundPainter` | Painter |  |
| `PasswordField[Disabled].borderPainter` | Painter |  |
| `PasswordField[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `PasswordField[Enabled].backgroundPainter` | Painter |  |
| `PasswordField[Enabled].borderPainter` | Painter |  |
| `PasswordField[Focused].borderPainter` | Painter |  |
| `PasswordField[Selected].backgroundPainter` | Painter |  |
| `PasswordField[Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |

#### InternalFrame

| Key | Value | Preview |
| --- | --- | --- |
| `InternalFrame.States` | Enabled,WindowFocused |  |
| `InternalFrame.WindowFocused` | WindowFocused |  |
| `InternalFrame.background` | ``` #d6d9df (214,217,223) ``` |  |
| `InternalFrame.contentMargins` | Insets (1,6,6,6) |  |
| `InternalFrame.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `InternalFrame.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `InternalFrame.font` | Font "SansSerif 12 |  |
| `InternalFrame.foreground` | ``` #000000 (0,0,0) ``` |  |
| `InternalFrame.titleFont` | Font "SansSerif 12 Bold |  |
| `InternalFrame.windowBindings` | [Ljava.lang.Object;@35cf7491 |  |
| `InternalFrame:InternalFrameTitlePane.States` | Enabled,WindowFocused |  |
| `InternalFrame:InternalFrameTitlePane.WindowFocused` | WindowFocused |  |
| `InternalFrame:InternalFrameTitlePane.contentMargins` | Insets (3,0,3,0) |  |
| `InternalFrame:InternalFrameTitlePane.titleAlignment` | CENTER |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.closeButton".States` | Enabled,MouseOver,Pressed,Disabled,Focused,Selected,WindowNotFocused |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.closeButton".WindowNotFocused` | WindowNotFocused |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.closeButton".contentMargins` | Insets (9,9,9,9) |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.closeButton"[Disabled].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.closeButton"[Enabled+WindowNotFocused].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.closeButton"[Enabled].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.closeButton"[MouseOver+WindowNotFocused].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.closeButton"[MouseOver].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.closeButton"[Pressed+WindowNotFocused].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.closeButton"[Pressed].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.iconifyButton".States` | Enabled,MouseOver,Pressed,Disabled,Focused,Selected,WindowNotFocused |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.iconifyButton".WindowNotFocused` | WindowNotFocused |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.iconifyButton".contentMargins` | Insets (9,9,9,9) |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.iconifyButton"[Disabled].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.iconifyButton"[Enabled+WindowNotFocused].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.iconifyButton"[Enabled].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.iconifyButton"[MouseOver+WindowNotFocused].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.iconifyButton"[MouseOver].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.iconifyButton"[Pressed+WindowNotFocused].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.iconifyButton"[Pressed].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton".States` | Enabled,MouseOver,Pressed,Disabled,Focused,Selected,WindowNotFocused,WindowMaximized |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton".WindowMaximized` | WindowMaximized |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton".WindowNotFocused` | WindowNotFocused |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton".contentMargins` | Insets (9,9,9,9) |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton"[Disabled+WindowMaximized].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton"[Disabled].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton"[Enabled+WindowMaximized+WindowNotFocused].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton"[Enabled+WindowMaximized].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton"[Enabled+WindowNotFocused].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton"[Enabled].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton"[MouseOver+WindowMaximized+WindowNotFocused].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton"[MouseOver+WindowMaximized].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton"[MouseOver+WindowNotFocused].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton"[MouseOver].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton"[Pressed+WindowMaximized+WindowNotFocused].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton"[Pressed+WindowMaximized].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton"[Pressed+WindowNotFocused].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.maximizeButton"[Pressed].backgroundPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.menuButton".States` | Enabled,MouseOver,Pressed,Disabled,Focused,Selected,WindowNotFocused |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.menuButton".WindowNotFocused` | WindowNotFocused |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.menuButton".contentMargins` | Insets (0,0,0,0) |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.menuButton".icon` | Icon 19 x 18 |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.menuButton".test` | am InternalFrameTitlePane.menuButton |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.menuButton"[Disabled].iconPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.menuButton"[Enabled+WindowNotFocused].iconPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.menuButton"[Enabled].iconPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.menuButton"[MouseOver+WindowNotFocused].iconPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.menuButton"[MouseOver].iconPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.menuButton"[Pressed+WindowNotFocused].iconPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane:"InternalFrameTitlePane.menuButton"[Pressed].iconPainter` | Painter |  |
| `InternalFrame:InternalFrameTitlePane[Enabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `InternalFrame[Enabled+WindowFocused].backgroundPainter` | Painter |  |
| `InternalFrame[Enabled].backgroundPainter` | Painter |  |

#### Button

| Key | Value | Preview |
| --- | --- | --- |
| `Button.background` | ``` #d6d9df (214,217,223) ``` |  |
| `Button.contentMargins` | Insets (6,14,6,14) |  |
| `Button.defaultButtonFollowsFocus` | false |  |
| `Button.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `Button.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `Button.focusInputMap` |  |  |
| `Button.font` | Font "SansSerif 12 |  |
| `Button.foreground` | ``` #000000 (0,0,0) ``` |  |
| `Button[Default+Focused+MouseOver].backgroundPainter` | Painter |  |
| `Button[Default+Focused+Pressed].backgroundPainter` | Painter |  |
| `Button[Default+Focused].backgroundPainter` | Painter |  |
| `Button[Default+MouseOver].backgroundPainter` | Painter |  |
| `Button[Default+Pressed].backgroundPainter` | Painter |  |
| `Button[Default+Pressed].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `Button[Default].backgroundPainter` | Painter |  |
| `Button[Disabled].backgroundPainter` | Painter |  |
| `Button[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `Button[Enabled].backgroundPainter` | Painter |  |
| `Button[Focused+MouseOver].backgroundPainter` | Painter |  |
| `Button[Focused+Pressed].backgroundPainter` | Painter |  |
| `Button[Focused].backgroundPainter` | Painter |  |
| `Button[MouseOver].backgroundPainter` | Painter |  |
| `Button[Pressed].backgroundPainter` | Painter |  |

#### Panel

| Key | Value | Preview |
| --- | --- | --- |
| `Panel.background` | ``` #d6d9df (214,217,223) ``` |  |
| `Panel.contentMargins` | Insets (0,0,0,0) |  |
| `Panel.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `Panel.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `Panel.font` | Font "SansSerif 12 |  |
| `Panel.foreground` | ``` #000000 (0,0,0) ``` |  |
| `Panel.opaque` | true |  |

#### MenuBar

| Key | Value | Preview |
| --- | --- | --- |
| `MenuBar.background` | ``` #d6d9df (214,217,223) ``` |  |
| `MenuBar.contentMargins` | Insets (2,6,2,6) |  |
| `MenuBar.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `MenuBar.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `MenuBar.font` | Font "SansSerif 12 |  |
| `MenuBar.foreground` | ``` #000000 (0,0,0) ``` |  |
| `MenuBar.windowBindings` | [Ljava.lang.Object;@5421e554 |  |
| `MenuBar:Menu.contentMargins` | Insets (1,4,2,4) |  |
| `MenuBar:Menu:MenuItemAccelerator.contentMargins` | Insets (0,0,0,0) |  |
| `MenuBar:Menu[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `MenuBar:Menu[Enabled].textForeground` | ``` #232324 (35,35,36) ``` |  |
| `MenuBar:Menu[Selected].backgroundPainter` | Painter |  |
| `MenuBar:Menu[Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `MenuBar[Enabled].backgroundPainter` | Painter |  |
| `MenuBar[Enabled].borderPainter` | Painter |  |

#### ComboBox

| Key | Value | Preview |
| --- | --- | --- |
| `ComboBox.Editable` | Editable |  |
| `ComboBox.States` | Enabled,MouseOver,Pressed,Selected,Disabled,Focused,Editable |  |
| `ComboBox.ancestorInputMap` |  |  |
| `ComboBox.background` | ``` #d6d9df (214,217,223) ``` |  |
| `ComboBox.buttonWhenNotEditable` | true |  |
| `ComboBox.contentMargins` | Insets (0,0,0,0) |  |
| `ComboBox.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `ComboBox.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `ComboBox.font` | Font "SansSerif 12 |  |
| `ComboBox.forceOpaque` | true |  |
| `ComboBox.foreground` | ``` #000000 (0,0,0) ``` |  |
| `ComboBox.padding` | Insets (3,3,3,3) |  |
| `ComboBox.popupInsets` | Insets (-2,2,0,2) |  |
| `ComboBox.pressedWhenPopupVisible` | true |  |
| `ComboBox.rendererUseListColors` | false |  |
| `ComboBox.squareButton` | false |  |
| `ComboBox:"ComboBox.arrowButton".Editable` | Editable |  |
| `ComboBox:"ComboBox.arrowButton".States` | Enabled,MouseOver,Pressed,Disabled,Editable |  |
| `ComboBox:"ComboBox.arrowButton".contentMargins` | Insets (0,0,0,0) |  |
| `ComboBox:"ComboBox.arrowButton".size` | 19 |  |
| `ComboBox:"ComboBox.arrowButton"[Disabled+Editable].backgroundPainter` | Painter |  |
| `ComboBox:"ComboBox.arrowButton"[Disabled].foregroundPainter` | Painter |  |
| `ComboBox:"ComboBox.arrowButton"[Editable+Enabled].backgroundPainter` | Painter |  |
| `ComboBox:"ComboBox.arrowButton"[Editable+MouseOver].backgroundPainter` | Painter |  |
| `ComboBox:"ComboBox.arrowButton"[Editable+Pressed].backgroundPainter` | Painter |  |
| `ComboBox:"ComboBox.arrowButton"[Editable+Selected].backgroundPainter` | Painter |  |
| `ComboBox:"ComboBox.arrowButton"[Enabled].foregroundPainter` | Painter |  |
| `ComboBox:"ComboBox.arrowButton"[MouseOver].foregroundPainter` | Painter |  |
| `ComboBox:"ComboBox.arrowButton"[Pressed].foregroundPainter` | Painter |  |
| `ComboBox:"ComboBox.arrowButton"[Selected].foregroundPainter` | Painter |  |
| `ComboBox:"ComboBox.listRenderer".background` | ``` #ffffff (255,255,255) ``` |  |
| `ComboBox:"ComboBox.listRenderer".contentMargins` | Insets (2,4,2,4) |  |
| `ComboBox:"ComboBox.listRenderer".opaque` | true |  |
| `ComboBox:"ComboBox.listRenderer"[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `ComboBox:"ComboBox.listRenderer"[Selected].background` | ``` #39698a (57,105,138) ``` |  |
| `ComboBox:"ComboBox.listRenderer"[Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `ComboBox:"ComboBox.renderer".contentMargins` | Insets (2,4,2,4) |  |
| `ComboBox:"ComboBox.renderer"[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `ComboBox:"ComboBox.renderer"[Selected].background` | ``` #39698a (57,105,138) ``` |  |
| `ComboBox:"ComboBox.renderer"[Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `ComboBox:"ComboBox.textField".contentMargins` | Insets (0,6,0,3) |  |
| `ComboBox:"ComboBox.textField"[Disabled].backgroundPainter` | Painter |  |
| `ComboBox:"ComboBox.textField"[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `ComboBox:"ComboBox.textField"[Enabled].backgroundPainter` | Painter |  |
| `ComboBox:"ComboBox.textField"[Selected].backgroundPainter` | Painter |  |
| `ComboBox:"ComboBox.textField"[Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `ComboBox[Disabled+Editable].backgroundPainter` | Painter |  |
| `ComboBox[Disabled+Pressed].backgroundPainter` | Painter |  |
| `ComboBox[Disabled].backgroundPainter` | Painter |  |
| `ComboBox[Editable+Enabled].backgroundPainter` | Painter |  |
| `ComboBox[Editable+Focused].backgroundPainter` | Painter |  |
| `ComboBox[Editable+MouseOver].backgroundPainter` | Painter |  |
| `ComboBox[Editable+Pressed].backgroundPainter` | Painter |  |
| `ComboBox[Enabled+Selected].backgroundPainter` | Painter |  |
| `ComboBox[Enabled].backgroundPainter` | Painter |  |
| `ComboBox[Focused+MouseOver].backgroundPainter` | Painter |  |
| `ComboBox[Focused+Pressed].backgroundPainter` | Painter |  |
| `ComboBox[Focused].backgroundPainter` | Painter |  |
| `ComboBox[MouseOver].backgroundPainter` | Painter |  |
| `ComboBox[Pressed].backgroundPainter` | Painter |  |

#### ToolBarSeparator

| Key | Value | Preview |
| --- | --- | --- |
| `ToolBarSeparator.contentMargins` | Insets (2,0,3,0) |  |
| `ToolBarSeparator.textForeground` | ``` #9297a1 (146,151,161) ``` |  |
| `ToolBarSeparator[Enabled].backgroundPainter` | Painter |  |

#### Tree

| Key | Value | Preview |
| --- | --- | --- |
| `Tree.ancestorInputMap` |  |  |
| `Tree.background` | ``` #ffffff (255,255,255) ``` |  |
| `Tree.closedIcon` | Icon 16 x 16 |  |
| `Tree.collapsedIcon` | Icon 18 x 7 |  |
| `Tree.contentMargins` | Insets (0,0,0,0) |  |
| `Tree.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `Tree.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `Tree.drawHorizontalLines` | false |  |
| `Tree.drawVerticalLines` | false |  |
| `Tree.dropLineColor` | ``` #73a4d1 (115,164,209) ``` |  |
| `Tree.expandedIcon` | Icon 18 x 7 |  |
| `Tree.focusInputMap` |  |  |
| `Tree.focusInputMap.RightToLeft` |  |  |
| `Tree.font` | Font "SansSerif 12 |  |
| `Tree.foreground` | ``` #000000 (0,0,0) ``` |  |
| `Tree.leafIcon` | Icon 16 x 16 |  |
| `Tree.leftChildIndent` | 12 |  |
| `Tree.opaque` | true |  |
| `Tree.openIcon` | Icon 16 x 16 |  |
| `Tree.rendererFillBackground` | false |  |
| `Tree.rendererMargins` | Insets (2,0,1,5) |  |
| `Tree.rendererUseTreeColors` | true |  |
| `Tree.repaintWholeRow` | true |  |
| `Tree.rightChildIndent` | 4 |  |
| `Tree.rowHeight` | 0 |  |
| `Tree.selectionBackground` | ``` #39698a (57,105,138) ``` |  |
| `Tree.selectionForeground` | ``` #ffffff (255,255,255) ``` |  |
| `Tree.showRootHandles` | false |  |
| `Tree.textBackground` | ``` #ffffff (255,255,255) ``` |  |
| `Tree.textForeground` | ``` #000000 (0,0,0) ``` |  |
| `Tree:"Tree.cellRenderer".contentMargins` | Insets (0,0,0,0) |  |
| `Tree:"Tree.cellRenderer"[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `Tree:TreeCell.contentMargins` | Insets (0,0,0,0) |  |
| `Tree:TreeCell[Enabled+Focused].background` | ``` #ffffff (255,255,255) ``` |  |
| `Tree:TreeCell[Enabled+Focused].backgroundPainter` | Painter |  |
| `Tree:TreeCell[Enabled+Selected].backgroundPainter` | Painter |  |
| `Tree:TreeCell[Enabled+Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `Tree:TreeCell[Enabled].background` | ``` #ffffff (255,255,255) ``` |  |
| `Tree:TreeCell[Focused+Selected].backgroundPainter` | Painter |  |
| `Tree:TreeCell[Focused+Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `Tree[Enabled+Selected].collapsedIconPainter` | Painter |  |
| `Tree[Enabled+Selected].expandedIconPainter` | Painter |  |
| `Tree[Enabled].closedIconPainter` | Painter |  |
| `Tree[Enabled].collapsedIconPainter` | Painter |  |
| `Tree[Enabled].expandedIconPainter` | Painter |  |
| `Tree[Enabled].leafIconPainter` | Painter |  |
| `Tree[Enabled].openIconPainter` | Painter |  |

#### EditorPane

| Key | Value | Preview |
| --- | --- | --- |
| `EditorPane.background` | ``` #d6d9df (214,217,223) ``` |  |
| `EditorPane.contentMargins` | Insets (4,6,4,6) |  |
| `EditorPane.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `EditorPane.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `EditorPane.focusInputMap` |  |  |
| `EditorPane.font` | Font "SansSerif 12 |  |
| `EditorPane.foreground` | ``` #000000 (0,0,0) ``` |  |
| `EditorPane.opaque` | true |  |
| `EditorPane[Disabled].backgroundPainter` | Painter |  |
| `EditorPane[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `EditorPane[Enabled].backgroundPainter` | Painter |  |
| `EditorPane[Selected].backgroundPainter` | Painter |  |
| `EditorPane[Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |

#### CheckBox

| Key | Value | Preview |
| --- | --- | --- |
| `CheckBox.background` | ``` #d6d9df (214,217,223) ``` |  |
| `CheckBox.contentMargins` | Insets (0,0,0,0) |  |
| `CheckBox.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `CheckBox.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `CheckBox.focusInputMap` |  |  |
| `CheckBox.font` | Font "SansSerif 12 |  |
| `CheckBox.foreground` | ``` #000000 (0,0,0) ``` |  |
| `CheckBox.icon` | Icon 18 x 18 |  |
| `CheckBox[Disabled+Selected].iconPainter` | Painter |  |
| `CheckBox[Disabled].iconPainter` | Painter |  |
| `CheckBox[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `CheckBox[Enabled].iconPainter` | Painter |  |
| `CheckBox[Focused+MouseOver+Selected].iconPainter` | Painter |  |
| `CheckBox[Focused+MouseOver].iconPainter` | Painter |  |
| `CheckBox[Focused+Pressed+Selected].iconPainter` | Painter |  |
| `CheckBox[Focused+Pressed].iconPainter` | Painter |  |
| `CheckBox[Focused+Selected].iconPainter` | Painter |  |
| `CheckBox[Focused].iconPainter` | Painter |  |
| `CheckBox[MouseOver+Selected].iconPainter` | Painter |  |
| `CheckBox[MouseOver].iconPainter` | Painter |  |
| `CheckBox[Pressed+Selected].iconPainter` | Painter |  |
| `CheckBox[Pressed].iconPainter` | Painter |  |
| `CheckBox[Selected].iconPainter` | Painter |  |

#### ToggleButton

| Key | Value | Preview |
| --- | --- | --- |
| `ToggleButton.background` | ``` #d6d9df (214,217,223) ``` |  |
| `ToggleButton.contentMargins` | Insets (6,14,6,14) |  |
| `ToggleButton.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `ToggleButton.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `ToggleButton.focusInputMap` |  |  |
| `ToggleButton.font` | Font "SansSerif 12 |  |
| `ToggleButton.foreground` | ``` #000000 (0,0,0) ``` |  |
| `ToggleButton[Disabled+Selected].backgroundPainter` | Painter |  |
| `ToggleButton[Disabled+Selected].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `ToggleButton[Disabled].backgroundPainter` | Painter |  |
| `ToggleButton[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `ToggleButton[Enabled].backgroundPainter` | Painter |  |
| `ToggleButton[Focused+MouseOver+Selected].backgroundPainter` | Painter |  |
| `ToggleButton[Focused+MouseOver].backgroundPainter` | Painter |  |
| `ToggleButton[Focused+Pressed+Selected].backgroundPainter` | Painter |  |
| `ToggleButton[Focused+Pressed].backgroundPainter` | Painter |  |
| `ToggleButton[Focused+Selected].backgroundPainter` | Painter |  |
| `ToggleButton[Focused].backgroundPainter` | Painter |  |
| `ToggleButton[MouseOver+Selected].backgroundPainter` | Painter |  |
| `ToggleButton[MouseOver].backgroundPainter` | Painter |  |
| `ToggleButton[Pressed+Selected].backgroundPainter` | Painter |  |
| `ToggleButton[Pressed].backgroundPainter` | Painter |  |
| `ToggleButton[Selected].backgroundPainter` | Painter |  |

#### "Tree.cellEditor"

| Key | Value | Preview |
| --- | --- | --- |
| `"Tree.cellEditor".background` | ``` #ffffff (255,255,255) ``` |  |
| `"Tree.cellEditor".contentMargins` | Insets (2,5,2,5) |  |
| `"Tree.cellEditor".opaque` | true |  |
| `"Tree.cellEditor"[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `"Tree.cellEditor"[Enabled+Focused].backgroundPainter` | Painter |  |
| `"Tree.cellEditor"[Enabled].backgroundPainter` | Painter |  |
| `"Tree.cellEditor"[Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |

#### TabbedPane

| Key | Value | Preview |
| --- | --- | --- |
| `TabbedPane.ancestorInputMap` |  |  |
| `TabbedPane.background` | ``` #d6d9df (214,217,223) ``` |  |
| `TabbedPane.contentMargins` | Insets (0,0,0,0) |  |
| `TabbedPane.darkShadow` | ``` #000000 (0,0,0) ``` |  |
| `TabbedPane.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `TabbedPane.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `TabbedPane.extendTabsToBase` | true |  |
| `TabbedPane.focusInputMap` |  |  |
| `TabbedPane.font` | Font "SansSerif 12 |  |
| `TabbedPane.foreground` | ``` #000000 (0,0,0) ``` |  |
| `TabbedPane.highlight` | ``` #ffffff (255,255,255) ``` |  |
| `TabbedPane.isTabRollover` | true |  |
| `TabbedPane.nudgeSelectedLabel` | false |  |
| `TabbedPane.shadow` | ``` #8e8f91 (142,143,145) ``` |  |
| `TabbedPane.tabAreaStatesMatchSelectedTab` | true |  |
| `TabbedPane.tabOverlap` | -1 |  |
| `TabbedPane.tabRunOverlay` | 2 |  |
| `TabbedPane.useBasicArrows` | true |  |
| `TabbedPane:TabbedPaneContent.contentMargins` | Insets (0,0,0,0) |  |
| `TabbedPane:TabbedPaneTab.contentMargins` | Insets (2,8,3,8) |  |
| `TabbedPane:TabbedPaneTabArea.contentMargins` | Insets (3,10,4,10) |  |
| `TabbedPane:TabbedPaneTabArea[Disabled].backgroundPainter` | Painter |  |
| `TabbedPane:TabbedPaneTabArea[Enabled+MouseOver].backgroundPainter` | Painter |  |
| `TabbedPane:TabbedPaneTabArea[Enabled+Pressed].backgroundPainter` | Painter |  |
| `TabbedPane:TabbedPaneTabArea[Enabled].backgroundPainter` | Painter |  |
| `TabbedPane:TabbedPaneTab[Disabled+Selected].backgroundPainter` | Painter |  |
| `TabbedPane:TabbedPaneTab[Disabled].backgroundPainter` | Painter |  |
| `TabbedPane:TabbedPaneTab[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `TabbedPane:TabbedPaneTab[Enabled+MouseOver].backgroundPainter` | Painter |  |
| `TabbedPane:TabbedPaneTab[Enabled+Pressed].backgroundPainter` | Painter |  |
| `TabbedPane:TabbedPaneTab[Enabled].backgroundPainter` | Painter |  |
| `TabbedPane:TabbedPaneTab[Focused+MouseOver+Selected].backgroundPainter` | Painter |  |
| `TabbedPane:TabbedPaneTab[Focused+Pressed+Selected].backgroundPainter` | Painter |  |
| `TabbedPane:TabbedPaneTab[Focused+Pressed+Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `TabbedPane:TabbedPaneTab[Focused+Selected].backgroundPainter` | Painter |  |
| `TabbedPane:TabbedPaneTab[MouseOver+Selected].backgroundPainter` | Painter |  |
| `TabbedPane:TabbedPaneTab[Pressed+Selected].backgroundPainter` | Painter |  |
| `TabbedPane:TabbedPaneTab[Pressed+Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `TabbedPane:TabbedPaneTab[Selected].backgroundPainter` | Painter |  |

#### TableHeader

| Key | Value | Preview |
| --- | --- | --- |
| `TableHeader.ancestorInputMap` |  |  |
| `TableHeader.background` | ``` #d6d9df (214,217,223) ``` |  |
| `TableHeader.contentMargins` | Insets (0,0,0,0) |  |
| `TableHeader.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `TableHeader.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `TableHeader.font` | Font "SansSerif 12 |  |
| `TableHeader.foreground` | ``` #000000 (0,0,0) ``` |  |
| `TableHeader.opaque` | true |  |
| `TableHeader.rightAlignSortArrow` | true |  |
| `TableHeader:"TableHeader.renderer".Sorted` | Sorted |  |
| `TableHeader:"TableHeader.renderer".States` | Enabled,MouseOver,Pressed,Disabled,Focused,Selected,Sorted |  |
| `TableHeader:"TableHeader.renderer".contentMargins` | Insets (2,5,4,5) |  |
| `TableHeader:"TableHeader.renderer".opaque` | true |  |
| `TableHeader:"TableHeader.renderer"[Disabled+Sorted].backgroundPainter` | Painter |  |
| `TableHeader:"TableHeader.renderer"[Disabled].backgroundPainter` | Painter |  |
| `TableHeader:"TableHeader.renderer"[Enabled+Focused+Sorted].backgroundPainter` | Painter |  |
| `TableHeader:"TableHeader.renderer"[Enabled+Focused].backgroundPainter` | Painter |  |
| `TableHeader:"TableHeader.renderer"[Enabled+Sorted].backgroundPainter` | Painter |  |
| `TableHeader:"TableHeader.renderer"[Enabled].backgroundPainter` | Painter |  |
| `TableHeader:"TableHeader.renderer"[MouseOver].backgroundPainter` | Painter |  |
| `TableHeader:"TableHeader.renderer"[Pressed].backgroundPainter` | Painter |  |
| `TableHeader[Enabled].ascendingSortIconPainter` | Painter |  |
| `TableHeader[Enabled].descendingSortIconPainter` | Painter |  |

#### List

| Key | Value | Preview |
| --- | --- | --- |
| `List.background` | ``` #ffffff (255,255,255) ``` |  |
| `List.cellNoFocusBorder` | Border Insets(2,5,2,5) |  |
| `List.contentMargins` | Insets (0,0,0,0) |  |
| `List.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `List.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `List.dropLineColor` | ``` #73a4d1 (115,164,209) ``` |  |
| `List.focusCellHighlightBorder` | Border Insets(2,5,2,5) |  |
| `List.focusInputMap` |  |  |
| `List.focusInputMap.RightToLeft` |  |  |
| `List.font` | Font "SansSerif 12 |  |
| `List.foreground` | ``` #000000 (0,0,0) ``` |  |
| `List.opaque` | true |  |
| `List.rendererUseListColors` | true |  |
| `List.rendererUseUIBorder` | true |  |
| `List:"List.cellRenderer".contentMargins` | Insets (0,0,0,0) |  |
| `List:"List.cellRenderer".opaque` | true |  |
| `List:"List.cellRenderer"[Disabled].background` | ``` #39698a (57,105,138) ``` |  |
| `List:"List.cellRenderer"[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `List[Disabled+Selected].textBackground` | ``` #39698a (57,105,138) ``` |  |
| `List[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `List[Selected].textBackground` | ``` #39698a (57,105,138) ``` |  |
| `List[Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |

#### PopupMenu

| Key | Value | Preview |
| --- | --- | --- |
| `PopupMenu.background` | ``` #d6d9df (214,217,223) ``` |  |
| `PopupMenu.consumeEventOnClose` | true |  |
| `PopupMenu.contentMargins` | Insets (6,1,6,1) |  |
| `PopupMenu.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `PopupMenu.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `PopupMenu.font` | Font "SansSerif 12 |  |
| `PopupMenu.foreground` | ``` #000000 (0,0,0) ``` |  |
| `PopupMenu.opaque` | true |  |
| `PopupMenu.selectedWindowInputMapBindings` | [Ljava.lang.Object;@215f7107 |  |
| `PopupMenu.selectedWindowInputMapBindings.RightToLeft` | [Ljava.lang.Object;@1fa12495 |  |
| `PopupMenu[Disabled].backgroundPainter` | Painter |  |
| `PopupMenu[Enabled].backgroundPainter` | Painter |  |

#### ToolTip

| Key | Value | Preview |
| --- | --- | --- |
| `ToolTip.background` | ``` #d6d9df (214,217,223) ``` |  |
| `ToolTip.contentMargins` | Insets (4,4,4,4) |  |
| `ToolTip.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `ToolTip.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `ToolTip.font` | Font "SansSerif 12 |  |
| `ToolTip.foreground` | ``` #000000 (0,0,0) ``` |  |
| `ToolTip[Enabled].backgroundPainter` | Painter |  |

#### Separator

| Key | Value | Preview |
| --- | --- | --- |
| `Separator.background` | ``` #d6d9df (214,217,223) ``` |  |
| `Separator.contentMargins` | Insets (0,0,0,0) |  |
| `Separator.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `Separator.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `Separator.font` | Font "SansSerif 12 |  |
| `Separator.foreground` | ``` #000000 (0,0,0) ``` |  |
| `Separator[Enabled].backgroundPainter` | Painter |  |

#### RadioButtonMenuItem

| Key | Value | Preview |
| --- | --- | --- |
| `RadioButtonMenuItem.background` | ``` #d6d9df (214,217,223) ``` |  |
| `RadioButtonMenuItem.checkIcon` | Icon 9 x 10 |  |
| `RadioButtonMenuItem.contentMargins` | Insets (1,12,2,13) |  |
| `RadioButtonMenuItem.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `RadioButtonMenuItem.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `RadioButtonMenuItem.font` | Font "SansSerif 12 |  |
| `RadioButtonMenuItem.foreground` | ``` #232324 (35,35,36) ``` |  |
| `RadioButtonMenuItem.textIconGap` | 5 |  |
| `RadioButtonMenuItem:MenuItemAccelerator.contentMargins` | Insets (0,0,0,0) |  |
| `RadioButtonMenuItem:MenuItemAccelerator[MouseOver].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `RadioButtonMenuItem[Disabled+Selected].checkIconPainter` | Painter |  |
| `RadioButtonMenuItem[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `RadioButtonMenuItem[Enabled+Selected].checkIconPainter` | Painter |  |
| `RadioButtonMenuItem[Enabled].textForeground` | ``` #232324 (35,35,36) ``` |  |
| `RadioButtonMenuItem[MouseOver+Selected].backgroundPainter` | Painter |  |
| `RadioButtonMenuItem[MouseOver+Selected].checkIconPainter` | Painter |  |
| `RadioButtonMenuItem[MouseOver+Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `RadioButtonMenuItem[MouseOver].backgroundPainter` | Painter |  |
| `RadioButtonMenuItem[MouseOver].textForeground` | ``` #ffffff (255,255,255) ``` |  |

#### RadioButton

| Key | Value | Preview |
| --- | --- | --- |
| `RadioButton.background` | ``` #d6d9df (214,217,223) ``` |  |
| `RadioButton.contentMargins` | Insets (0,0,0,0) |  |
| `RadioButton.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `RadioButton.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `RadioButton.focusInputMap` |  |  |
| `RadioButton.font` | Font "SansSerif 12 |  |
| `RadioButton.foreground` | ``` #000000 (0,0,0) ``` |  |
| `RadioButton.icon` | Icon 18 x 18 |  |
| `RadioButton[Disabled+Selected].iconPainter` | Painter |  |
| `RadioButton[Disabled].iconPainter` | Painter |  |
| `RadioButton[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `RadioButton[Enabled].iconPainter` | Painter |  |
| `RadioButton[Focused+MouseOver+Selected].iconPainter` | Painter |  |
| `RadioButton[Focused+MouseOver].iconPainter` | Painter |  |
| `RadioButton[Focused+Pressed+Selected].iconPainter` | Painter |  |
| `RadioButton[Focused+Pressed].iconPainter` | Painter |  |
| `RadioButton[Focused+Selected].iconPainter` | Painter |  |
| `RadioButton[Focused].iconPainter` | Painter |  |
| `RadioButton[MouseOver+Selected].iconPainter` | Painter |  |
| `RadioButton[MouseOver].iconPainter` | Painter |  |
| `RadioButton[Pressed+Selected].iconPainter` | Painter |  |
| `RadioButton[Pressed].iconPainter` | Painter |  |
| `RadioButton[Selected].iconPainter` | Painter |  |

#### ToolBar

| Key | Value | Preview |
| --- | --- | --- |
| `ToolBar.East` | East |  |
| `ToolBar.North` | North |  |
| `ToolBar.South` | South |  |
| `ToolBar.States` | North,East,West,South |  |
| `ToolBar.West` | West |  |
| `ToolBar.ancestorInputMap` |  |  |
| `ToolBar.background` | ``` #d6d9df (214,217,223) ``` |  |
| `ToolBar.contentMargins` | Insets (2,2,2,2) |  |
| `ToolBar.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `ToolBar.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `ToolBar.font` | Font "SansSerif 12 |  |
| `ToolBar.foreground` | ``` #000000 (0,0,0) ``` |  |
| `ToolBar.handleIcon` | Icon 11 x 38 |  |
| `ToolBar.opaque` | true |  |
| `ToolBar:Button.contentMargins` | Insets (4,4,4,4) |  |
| `ToolBar:Button[Focused+MouseOver].backgroundPainter` | Painter |  |
| `ToolBar:Button[Focused+Pressed].backgroundPainter` | Painter |  |
| `ToolBar:Button[Focused].backgroundPainter` | Painter |  |
| `ToolBar:Button[MouseOver].backgroundPainter` | Painter |  |
| `ToolBar:Button[Pressed].backgroundPainter` | Painter |  |
| `ToolBar:ToggleButton.contentMargins` | Insets (4,4,4,4) |  |
| `ToolBar:ToggleButton[Disabled+Selected].backgroundPainter` | Painter |  |
| `ToolBar:ToggleButton[Disabled+Selected].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `ToolBar:ToggleButton[Focused+MouseOver+Selected].backgroundPainter` | Painter |  |
| `ToolBar:ToggleButton[Focused+MouseOver].backgroundPainter` | Painter |  |
| `ToolBar:ToggleButton[Focused+Pressed+Selected].backgroundPainter` | Painter |  |
| `ToolBar:ToggleButton[Focused+Pressed].backgroundPainter` | Painter |  |
| `ToolBar:ToggleButton[Focused+Selected].backgroundPainter` | Painter |  |
| `ToolBar:ToggleButton[Focused].backgroundPainter` | Painter |  |
| `ToolBar:ToggleButton[MouseOver+Selected].backgroundPainter` | Painter |  |
| `ToolBar:ToggleButton[MouseOver].backgroundPainter` | Painter |  |
| `ToolBar:ToggleButton[Pressed+Selected].backgroundPainter` | Painter |  |
| `ToolBar:ToggleButton[Pressed].backgroundPainter` | Painter |  |
| `ToolBar:ToggleButton[Selected].backgroundPainter` | Painter |  |
| `ToolBar[East].borderPainter` | Painter |  |
| `ToolBar[Enabled].handleIconPainter` | Painter |  |
| `ToolBar[North].borderPainter` | Painter |  |
| `ToolBar[South].borderPainter` | Painter |  |
| `ToolBar[West].borderPainter` | Painter |  |

#### "ComboBox.scrollPane"

| Key | Value | Preview |
| --- | --- | --- |
| `"ComboBox.scrollPane".contentMargins` | Insets (0,0,0,0) |  |

#### ScrollPane

| Key | Value | Preview |
| --- | --- | --- |
| `ScrollPane.ancestorInputMap` |  |  |
| `ScrollPane.ancestorInputMap.RightToLeft` |  |  |
| `ScrollPane.background` | ``` #d6d9df (214,217,223) ``` |  |
| `ScrollPane.contentMargins` | Insets (3,3,3,3) |  |
| `ScrollPane.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `ScrollPane.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `ScrollPane.font` | Font "SansSerif 12 |  |
| `ScrollPane.foreground` | ``` #000000 (0,0,0) ``` |  |
| `ScrollPane.useChildTextComponentFocus` | true |  |
| `ScrollPane[Enabled+Focused].borderPainter` | Painter |  |
| `ScrollPane[Enabled].borderPainter` | Painter |  |

#### CheckBoxMenuItem

| Key | Value | Preview |
| --- | --- | --- |
| `CheckBoxMenuItem.background` | ``` #d6d9df (214,217,223) ``` |  |
| `CheckBoxMenuItem.checkIcon` | Icon 9 x 10 |  |
| `CheckBoxMenuItem.contentMargins` | Insets (1,12,2,13) |  |
| `CheckBoxMenuItem.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `CheckBoxMenuItem.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `CheckBoxMenuItem.font` | Font "SansSerif 12 |  |
| `CheckBoxMenuItem.foreground` | ``` #232324 (35,35,36) ``` |  |
| `CheckBoxMenuItem.textIconGap` | 5 |  |
| `CheckBoxMenuItem:MenuItemAccelerator.contentMargins` | Insets (0,0,0,0) |  |
| `CheckBoxMenuItem:MenuItemAccelerator[MouseOver].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `CheckBoxMenuItem[Disabled+Selected].checkIconPainter` | Painter |  |
| `CheckBoxMenuItem[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `CheckBoxMenuItem[Enabled+Selected].checkIconPainter` | Painter |  |
| `CheckBoxMenuItem[Enabled].textForeground` | ``` #232324 (35,35,36) ``` |  |
| `CheckBoxMenuItem[MouseOver+Selected].backgroundPainter` | Painter |  |
| `CheckBoxMenuItem[MouseOver+Selected].checkIconPainter` | Painter |  |
| `CheckBoxMenuItem[MouseOver+Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `CheckBoxMenuItem[MouseOver].backgroundPainter` | Painter |  |
| `CheckBoxMenuItem[MouseOver].textForeground` | ``` #ffffff (255,255,255) ``` |  |

#### Viewport

| Key | Value | Preview |
| --- | --- | --- |
| `Viewport.background` | ``` #d6d9df (214,217,223) ``` |  |
| `Viewport.contentMargins` | Insets (0,0,0,0) |  |
| `Viewport.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `Viewport.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `Viewport.font` | Font "SansSerif 12 |  |
| `Viewport.foreground` | ``` #000000 (0,0,0) ``` |  |
| `Viewport.opaque` | true |  |

#### TextField

| Key | Value | Preview |
| --- | --- | --- |
| `TextField.background` | ``` #ffffff (255,255,255) ``` |  |
| `TextField.contentMargins` | Insets (6,6,6,6) |  |
| `TextField.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `TextField.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `TextField.focusInputMap` |  |  |
| `TextField.font` | Font "SansSerif 12 |  |
| `TextField.foreground` | ``` #000000 (0,0,0) ``` |  |
| `TextField[Disabled].backgroundPainter` | Painter |  |
| `TextField[Disabled].borderPainter` | Painter |  |
| `TextField[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `TextField[Enabled].backgroundPainter` | Painter |  |
| `TextField[Enabled].borderPainter` | Painter |  |
| `TextField[Focused].borderPainter` | Painter |  |
| `TextField[Selected].backgroundPainter` | Painter |  |
| `TextField[Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |

#### SplitPane

| Key | Value | Preview |
| --- | --- | --- |
| `SplitPane.States` | Enabled,MouseOver,Pressed,Disabled,Focused,Selected,Vertical |  |
| `SplitPane.Vertical` | Vertical |  |
| `SplitPane.ancestorInputMap` |  |  |
| `SplitPane.background` | ``` #d6d9df (214,217,223) ``` |  |
| `SplitPane.centerOneTouchButtons` | true |  |
| `SplitPane.contentMargins` | Insets (1,1,1,1) |  |
| `SplitPane.continuousLayout` | true |  |
| `SplitPane.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `SplitPane.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `SplitPane.dividerSize` | 10 |  |
| `SplitPane.font` | Font "SansSerif 12 |  |
| `SplitPane.foreground` | ``` #000000 (0,0,0) ``` |  |
| `SplitPane.oneTouchButtonOffset` | 30 |  |
| `SplitPane.oneTouchExpandable` | false |  |
| `SplitPane.size` | 10 |  |
| `SplitPane:SplitPaneDivider.States` | Enabled,MouseOver,Pressed,Disabled,Focused,Selected,Vertical |  |
| `SplitPane:SplitPaneDivider.Vertical` | Vertical |  |
| `SplitPane:SplitPaneDivider.contentMargins` | Insets (0,0,0,0) |  |
| `SplitPane:SplitPaneDivider[Enabled+Vertical].foregroundPainter` | Painter |  |
| `SplitPane:SplitPaneDivider[Enabled].backgroundPainter` | Painter |  |
| `SplitPane:SplitPaneDivider[Enabled].foregroundPainter` | Painter |  |
| `SplitPane:SplitPaneDivider[Focused].backgroundPainter` | Painter |  |

#### MenuItem

| Key | Value | Preview |
| --- | --- | --- |
| `MenuItem.background` | ``` #d6d9df (214,217,223) ``` |  |
| `MenuItem.contentMargins` | Insets (1,12,2,13) |  |
| `MenuItem.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `MenuItem.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `MenuItem.font` | Font "SansSerif 12 |  |
| `MenuItem.foreground` | ``` #232324 (35,35,36) ``` |  |
| `MenuItem.textIconGap` | 5 |  |
| `MenuItem:MenuItemAccelerator.contentMargins` | Insets (0,0,0,0) |  |
| `MenuItem:MenuItemAccelerator[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `MenuItem:MenuItemAccelerator[MouseOver].textForeground` | ``` #ffffff (255,255,255) ``` |  |
| `MenuItem[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `MenuItem[Enabled].textForeground` | ``` #232324 (35,35,36) ``` |  |
| `MenuItem[MouseOver].backgroundPainter` | Painter |  |
| `MenuItem[MouseOver].textForeground` | ``` #ffffff (255,255,255) ``` |  |

#### OptionPane

| Key | Value | Preview |
| --- | --- | --- |
| `OptionPane.background` | ``` #d6d9df (214,217,223) ``` |  |
| `OptionPane.buttonOrientation` | 4 |  |
| `OptionPane.contentMargins` | Insets (15,15,15,15) |  |
| `OptionPane.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `OptionPane.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `OptionPane.errorIcon` | Icon 48 x 48 |  |
| `OptionPane.font` | Font "SansSerif 12 |  |
| `OptionPane.foreground` | ``` #000000 (0,0,0) ``` |  |
| `OptionPane.informationIcon` | Icon 48 x 48 |  |
| `OptionPane.isYesLast` | true |  |
| `OptionPane.messageAnchor` | 17 |  |
| `OptionPane.opaque` | true |  |
| `OptionPane.questionIcon` | Icon 48 x 48 |  |
| `OptionPane.sameSizeButtons` | false |  |
| `OptionPane.separatorPadding` | 0 |  |
| `OptionPane.warningIcon` | Icon 48 x 48 |  |
| `OptionPane.windowBindings` | [Ljava.lang.Object;@3ff2cea2 |  |
| `OptionPane:"OptionPane.messageArea".contentMargins` | Insets (0,0,10,0) |  |
| `OptionPane:"OptionPane.messageArea":"OptionPane.label".contentMargins` | Insets (0,10,10,10) |  |
| `OptionPane:"OptionPane.messageArea":"OptionPane.label"[Enabled].backgroundPainter` | Painter |  |
| `OptionPane:"OptionPane.separator".contentMargins` | Insets (1,0,0,0) |  |
| `OptionPane[Enabled].errorIconPainter` | Painter |  |
| `OptionPane[Enabled].informationIconPainter` | Painter |  |
| `OptionPane[Enabled].questionIconPainter` | Painter |  |
| `OptionPane[Enabled].warningIconPainter` | Painter |  |

#### ArrowButton

| Key | Value | Preview |
| --- | --- | --- |
| `ArrowButton.background` | ``` #d6d9df (214,217,223) ``` |  |
| `ArrowButton.contentMargins` | Insets (0,0,0,0) |  |
| `ArrowButton.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `ArrowButton.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `ArrowButton.font` | Font "SansSerif 12 |  |
| `ArrowButton.foreground` | ``` #000000 (0,0,0) ``` |  |
| `ArrowButton.size` | 16 |  |
| `ArrowButton[Disabled].foregroundPainter` | Painter |  |
| `ArrowButton[Enabled].foregroundPainter` | Painter |  |

#### Label

| Key | Value | Preview |
| --- | --- | --- |
| `Label.background` | ``` #d6d9df (214,217,223) ``` |  |
| `Label.contentMargins` | Insets (0,0,0,0) |  |
| `Label.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `Label.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `Label.font` | Font "SansSerif 12 |  |
| `Label.foreground` | ``` #000000 (0,0,0) ``` |  |
| `Label[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |

#### ProgressBar

| Key | Value | Preview |
| --- | --- | --- |
| `ProgressBar.Finished` | Finished |  |
| `ProgressBar.Indeterminate` | Indeterminate |  |
| `ProgressBar.States` | Enabled,Disabled,Indeterminate,Finished |  |
| `ProgressBar.background` | ``` #d6d9df (214,217,223) ``` |  |
| `ProgressBar.contentMargins` | Insets (0,0,0,0) |  |
| `ProgressBar.cycleTime` | 250 |  |
| `ProgressBar.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `ProgressBar.disabledText` | ``` #8e8f91 (142,143,145) ``` |  |
| `ProgressBar.font` | Font "SansSerif 12 |  |
| `ProgressBar.foreground` | ``` #000000 (0,0,0) ``` |  |
| `ProgressBar.horizontalSize` | Dimension (150,19) |  |
| `ProgressBar.paintOutsideClip` | true |  |
| `ProgressBar.rotateText` | true |  |
| `ProgressBar.tileWhenIndeterminate` | true |  |
| `ProgressBar.tileWidth` | 27 |  |
| `ProgressBar.vertictalSize` | Dimension (19,150) |  |
| `ProgressBar[Disabled+Finished].foregroundPainter` | Painter |  |
| `ProgressBar[Disabled+Indeterminate].foregroundPainter` | Painter |  |
| `ProgressBar[Disabled+Indeterminate].progressPadding` | 3 |  |
| `ProgressBar[Disabled].backgroundPainter` | Painter |  |
| `ProgressBar[Disabled].foregroundPainter` | Painter |  |
| `ProgressBar[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `ProgressBar[Enabled+Finished].foregroundPainter` | Painter |  |
| `ProgressBar[Enabled+Indeterminate].foregroundPainter` | Painter |  |
| `ProgressBar[Enabled+Indeterminate].progressPadding` | 3 |  |
| `ProgressBar[Enabled].backgroundPainter` | Painter |  |
| `ProgressBar[Enabled].foregroundPainter` | Painter |  |

#### ScrollBar

| Key | Value | Preview |
| --- | --- | --- |
| `ScrollBar.ancestorInputMap` |  |  |
| `ScrollBar.ancestorInputMap.RightToLeft` |  |  |
| `ScrollBar.background` | ``` #d6d9df (214,217,223) ``` |  |
| `ScrollBar.contentMargins` | Insets (0,0,0,0) |  |
| `ScrollBar.decrementButtonGap` | -8 |  |
| `ScrollBar.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `ScrollBar.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `ScrollBar.font` | Font "SansSerif 12 |  |
| `ScrollBar.foreground` | ``` #000000 (0,0,0) ``` |  |
| `ScrollBar.incrementButtonGap` | -8 |  |
| `ScrollBar.maximumThumbSize` | Dimension (1000,1000) |  |
| `ScrollBar.minimumThumbSize` | Dimension (29,29) |  |
| `ScrollBar.opaque` | true |  |
| `ScrollBar.thumbHeight` | 15 |  |
| `ScrollBar:"ScrollBar.button".contentMargins` | Insets (0,0,0,0) |  |
| `ScrollBar:"ScrollBar.button".size` | 25 |  |
| `ScrollBar:"ScrollBar.button"[Disabled].foregroundPainter` | Painter |  |
| `ScrollBar:"ScrollBar.button"[Enabled].foregroundPainter` | Painter |  |
| `ScrollBar:"ScrollBar.button"[MouseOver].foregroundPainter` | Painter |  |
| `ScrollBar:"ScrollBar.button"[Pressed].foregroundPainter` | Painter |  |
| `ScrollBar:ScrollBarThumb.contentMargins` | Insets (0,0,0,0) |  |
| `ScrollBar:ScrollBarThumb[Enabled].backgroundPainter` | Painter |  |
| `ScrollBar:ScrollBarThumb[MouseOver].backgroundPainter` | Painter |  |
| `ScrollBar:ScrollBarThumb[Pressed].backgroundPainter` | Painter |  |
| `ScrollBar:ScrollBarTrack.contentMargins` | Insets (0,0,0,0) |  |
| `ScrollBar:ScrollBarTrack[Disabled].backgroundPainter` | Painter |  |
| `ScrollBar:ScrollBarTrack[Enabled].backgroundPainter` | Painter |  |

#### "Table.editor"

| Key | Value | Preview |
| --- | --- | --- |
| `"Table.editor".background` | ``` #ffffff (255,255,255) ``` |  |
| `"Table.editor".contentMargins` | Insets (3,5,3,5) |  |
| `"Table.editor".opaque` | true |  |
| `"Table.editor"[Disabled].textForeground` | ``` #8e8f91 (142,143,145) ``` |  |
| `"Table.editor"[Enabled+Focused].backgroundPainter` | Painter |  |
| `"Table.editor"[Enabled].backgroundPainter` | Painter |  |
| `"Table.editor"[Selected].textForeground` | ``` #ffffff (255,255,255) ``` |  |

### Others

| Key | Value | Preview |
| --- | --- | --- |
| `FileView.computerIcon` | Icon 16 x 16 |  |
| `FileView.directoryIcon` | Icon 16 x 16 |  |
| `FileView.fileIcon` | Icon 16 x 16 |  |
| `FileView.floppyDriveIcon` | Icon 16 x 16 |  |
| `FileView.fullRowSelection` | true |  |
| `FileView.hardDriveIcon` | Icon 16 x 16 |  |
| `ScrollBarThumb.background` | ``` #d6d9df (214,217,223) ``` |  |
| `ScrollBarThumb.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `ScrollBarThumb.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `ScrollBarThumb.font` | Font "SansSerif 12 |  |
| `ScrollBarThumb.foreground` | ``` #000000 (0,0,0) ``` |  |
| `ScrollBarTrack.background` | ``` #d6d9df (214,217,223) ``` |  |
| `ScrollBarTrack.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `ScrollBarTrack.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `ScrollBarTrack.font` | Font "SansSerif 12 |  |
| `ScrollBarTrack.foreground` | ``` #000000 (0,0,0) ``` |  |
| `SliderThumb.background` | ``` #d6d9df (214,217,223) ``` |  |
| `SliderThumb.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `SliderThumb.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `SliderThumb.font` | Font "SansSerif 12 |  |
| `SliderThumb.foreground` | ``` #000000 (0,0,0) ``` |  |
| `SliderTrack.background` | ``` #d6d9df (214,217,223) ``` |  |
| `SliderTrack.disabled` | ``` #d6d9df (214,217,223) ``` |  |
| `SliderTrack.disabledText` | ``` #000000 (0,0,0) ``` |  |
| `SliderTrack.font` | Font "SansSerif 12 |  |
| `SliderTrack.foreground` | ``` #000000 (0,0,0) ``` |  |
| `TitledBorder.border` | Border Insets(10,10,10,10) |  |
| `TitledBorder.font` | Font "SansSerif 12 Bold |  |
| `TitledBorder.position` | ABOVE\_TOP |  |
| `TitledBorder.titleColor` | ``` #3b3b3b (59,59,59) ``` |  |
| `TitledBorder.titlePosition` | 1 |  |
| `defaultFont` | Font "SansSerif 12 |  |

### UI Classes

| Key | Value | Preview |
| --- | --- | --- |
| `ArrowButtonUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `ButtonUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `CheckBoxMenuItemUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `CheckBoxUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `ColorChooserUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `ComboBoxUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `DesktopIconUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `DesktopPaneUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `EditorPaneUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `FileChooserUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `FormattedTextFieldUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `InternalFrameTitlePaneUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `InternalFrameUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `LabelUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `ListUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `MenuBarUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `MenuItemUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `MenuUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `OptionPaneUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `PanelUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `PasswordFieldUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `PopupMenuSeparatorUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `PopupMenuUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `ProgressBarUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `RadioButtonMenuItemUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `RadioButtonUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `RootPaneUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `ScrollBarUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `ScrollPaneUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `SeparatorUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `SliderUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `SpinnerUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `SplitPaneUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `TabbedPaneUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `TableHeaderUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `TableUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `TextAreaUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `TextFieldUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `TextPaneUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `ToggleButtonUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `ToolBarSeparatorUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `ToolBarUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `ToolTipUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `TreeUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |
| `ViewportUI` | javax.swing.plaf.synth.SynthLookAndFeel |  |



A browser with JavaScript enabled is required for this page to operate properly.