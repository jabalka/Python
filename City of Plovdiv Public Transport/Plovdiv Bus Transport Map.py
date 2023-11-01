# This program is optimised for the PyCharm environment
import networkx as nx
import matplotlib.pyplot as plt
# Create a graph object
MyGraph = nx.Graph()
pos = nx.spring_layout(MyGraph)
# Add all the nodes
# Bus line 7 (green)
MyGraph.add_node('A7', npos=(-3, -22), ccn='#00FF00')
MyGraph.add_node('B7', npos=(50, -12), ccn='#00FF00')
MyGraph.add_node('C7', npos=(54, 3.8), ccn='#00FF00')
MyGraph.add_node('D7', npos=(52, 29), ccn='#00FF00')
MyGraph.add_node('E7', npos=(49, 42), ccn='#00FF00')
MyGraph.add_node('F7', npos=(46.5, 62), ccn='#00FF00')
MyGraph.add_node('G7', npos=(66.5, 80), ccn='#00FF00')
MyGraph.add_node('H7', npos=(80, 102), ccn='#00FF00')
MyGraph.add_node('I7', npos=(77, 120), ccn='#00FF00')
# Bus line 93 (orange)
MyGraph.add_node('A93', npos=(210, 70), ccn='#FFA500')
MyGraph.add_node('B93', npos=(185, 65), ccn='#FFA500')
MyGraph.add_node('C93', npos=(165, 69), ccn='#FFA500')
MyGraph.add_node('D93', npos=(165, 85), ccn='#FFA500')
MyGraph.add_node('E93', npos=(158, 96.5), ccn='#FFA500')
MyGraph.add_node('F93', npos=(139, 90), ccn='#FFA500')
MyGraph.add_node('G93', npos=(116, 83.5), ccn='#FFA500')
MyGraph.add_node('H93', npos=(96.5, 90), ccn='#FFA500')
MyGraph.add_node('I93', npos=(66.5, 84), ccn='#FFA500')
MyGraph.add_node('J93', npos=(30, 80), ccn='#FFA500')
MyGraph.add_node('K93', npos=(7, 72), ccn='#FFA500')
MyGraph.add_node('L93', npos=(-18, 66), ccn='#FFA500')
MyGraph.add_node('M93', npos=(-24, 83), ccn='#FFA500')
MyGraph.add_node('N93', npos=(-24, 95), ccn='#FFA500')
MyGraph.add_node('O93', npos=(-24, 120), ccn='#FFA500')
# Bus line 99 (blue)
MyGraph.add_node('A99', npos=(-35, 120), ccn='#00BFFF')
MyGraph.add_node('B99', npos=(-35, 95), ccn='#00BFFF')
MyGraph.add_node('C99', npos=(-35, 83), ccn='#00BFFF')
MyGraph.add_node('D99', npos=(-25, 60), ccn='#00BFFF')
MyGraph.add_node('E99', npos=(7, 66), ccn='#00BFFF')
MyGraph.add_node('F99', npos=(30, 74), ccn='#00BFFF')
MyGraph.add_node('G99', npos=(44, 70), ccn='#00BFFF')
MyGraph.add_node('H99', npos=(58, 43.5), ccn='#00BFFF')
MyGraph.add_node('I99', npos=(60, 30), ccn='#00BFFF')
MyGraph.add_node('J99', npos=(62, 4.8), ccn='#00BFFF')
MyGraph.add_node('K99', npos=(70, -8.5), ccn='#00BFFF')
MyGraph.add_node('L99', npos=(110, -2), ccn='#00BFFF')
MyGraph.add_node('M99', npos=(137, -2), ccn='#00BFFF')
MyGraph.add_node('N99', npos=(160, -9), ccn='#00BFFF')
MyGraph.add_node('O99', npos=(170, -24), ccn='#00BFFF')
# Bus line 9 (yellow)
MyGraph.add_node('A9', npos=(85, 120), ccn='#FFFF00')
MyGraph.add_node('B9', npos=(88, 102), ccn='#FFFF00')
MyGraph.add_node('C9', npos=(100, 94.5), ccn='#FFFF00')
MyGraph.add_node('D9', npos=(116, 88), ccn='#FFFF00')
MyGraph.add_node('E9', npos=(139, 95), ccn='#FFFF00')
MyGraph.add_node('F9', npos=(158, 101), ccn='#FFFF00')
MyGraph.add_node('G9', npos=(156.5, 85), ccn='#FFFF00')
MyGraph.add_node('H9', npos=(156.5, 69), ccn='#FFFF00')
MyGraph.add_node('I9', npos=(156.5, 47), ccn='#FFFF00')
MyGraph.add_node('J9', npos=(156.5, 15), ccn='#FFFF00')
MyGraph.add_node('K9', npos=(164, 0), ccn='#FFFF00')
MyGraph.add_node('L9', npos=(210, 12), ccn='#FFFF00')
# Connect nodes
# Green Line
MyGraph.add_edge('A7', 'B7', cce='#00FF00')
MyGraph.add_edge('B7', 'C7', cce='#00FF00')
MyGraph.add_edge('C7', 'D7', cce='#00FF00')
MyGraph.add_edge('D7', 'E7', cce='#00FF00')
MyGraph.add_edge('E7', 'F7', cce='#00FF00')
MyGraph.add_edge('F7', 'G7', cce='#00FF00')
MyGraph.add_edge('G7', 'H7', cce='#00FF00')
MyGraph.add_edge('H7', 'I7', cce='#00FF00')
# Orange Line
MyGraph.add_edge('A93', 'B93', cce='#FFA500')
MyGraph.add_edge('B93', 'C93', cce='#FFA500')
MyGraph.add_edge('C93', 'D93', cce='#FFA500')
MyGraph.add_edge('D93', 'E93', cce='#FFA500')
MyGraph.add_edge('E93', 'F93', cce='#FFA500')
MyGraph.add_edge('F93', 'G93', cce='#FFA500')
MyGraph.add_edge('G93', 'H93', cce='#FFA500')
MyGraph.add_edge('H93', 'I93', cce='#FFA500')
MyGraph.add_edge('I93', 'J93', cce='#FFA500')
MyGraph.add_edge('J93', 'K93', cce='#FFA500')
MyGraph.add_edge('K93', 'L93', cce='#FFA500')
MyGraph.add_edge('L93', 'M93', cce='#FFA500')
MyGraph.add_edge('M93', 'N93', cce='#FFA500')
MyGraph.add_edge('N93', 'O93', cce='#FFA500')
# Blue Line
MyGraph.add_edge('A99', 'B99', cce='#00BFFF')
MyGraph.add_edge('B99', 'C99', cce='#00BFFF')
MyGraph.add_edge('C99', 'D99', cce='#00BFFF')
MyGraph.add_edge('D99', 'E99', cce='#00BFFF')
MyGraph.add_edge('E99', 'F99', cce='#00BFFF')
MyGraph.add_edge('F99', 'G99', cce='#00BFFF')
MyGraph.add_edge('G99', 'H99', cce='#00BFFF')
MyGraph.add_edge('H99', 'I99', cce='#00BFFF')
MyGraph.add_edge('I99', 'J99', cce='#00BFFF')
MyGraph.add_edge('J99', 'K99', cce='#00BFFF')
MyGraph.add_edge('K99', 'L99', cce='#00BFFF')
MyGraph.add_edge('L99', 'M99', cce='#00BFFF')
MyGraph.add_edge('M99', 'N99', cce='#00BFFF')
MyGraph.add_edge('N99', 'O99', cce='#00BFFF')
# Yellow Line edge connected
MyGraph.add_edge('A9', 'B9', cce='#FFFF00')
MyGraph.add_edge('B9', 'C9', cce='#FFFF00')
MyGraph.add_edge('C9', 'D9', cce='#FFFF00')
MyGraph.add_edge('D9', 'E9', cce='#FFFF00')
MyGraph.add_edge('E9', 'F9', cce='#FFFF00')
MyGraph.add_edge('F9', 'G9', cce='#FFFF00')
MyGraph.add_edge('G9', 'H9', cce='#FFFF00')
MyGraph.add_edge('H9', 'I9', cce='#FFFF00')
MyGraph.add_edge('I9', 'J9', cce='#FFFF00')
MyGraph.add_edge('J9', 'K9', cce='#FFFF00')
MyGraph.add_edge('K9', 'L9', cce='#FFFF00')
# Extract attributes from the graph to dictionaries
pos = nx.get_node_attributes(MyGraph, 'npos')
nodecolour = nx.get_node_attributes(MyGraph, 'ccn')
edgecolour = nx.get_edge_attributes(MyGraph, 'cce')
# Place the dictionary values in lists
NodeList = list(nodecolour.values())
EdgeList = list(edgecolour.values())
# Set the size of the figure
plt.figure(figsize=(15, 13))
plt.axis([-57, 232, -40, 134])
# Bus Lines Numbers --------------------------------------------------
plt.text(213.5, 69.5, s='<93 Line', rotation=0, color = 'red', family='sans-serif', size=10, weight='bold')
plt.text(88.5, 119.5, s='<9 Line', rotation=0, color = 'red', family='sans-serif', size=10, weight='bold')
plt.text(-56, 119.5, s='99 Line>', rotation=-0, color = 'red', family='sans-serif', size=10, weight='bold')
plt.text(-22, -23, s='7 Line>', rotation=0, color = 'red', family='sans-serif', size=10, weight='bold')
 # All Bus stops' names displayed ---------------------------------------------------
plt.text(21.5, -30, s='Central\nRailway Station*', rotation=35, family='sans-serif', size=10)
plt.text(19.5, 3, s='Military Districts*', rotation=0, family='sans-serif', size=10)
plt.text(62, 40, s='*National Trade\n      School', rotation=0, family='sans-serif', size=10)
plt.text(50, 61, s='*Pianoto', rotation=0, family='sans-serif', size=10)
plt.text(91, 103, s='*Vodna Palata', rotation=35, family='sans-serif', size=10)
plt.text(103, 95, s='*Divinity School', rotation=35, family='sans-serif', size=10)
plt.text(189, 63, s='*Rositsa', rotation=0, family='sans-serif', size=10)
plt.text(133.5, 68.5, s='Cemetery*', rotation=0, family='sans-serif', size=10)
plt.text(169, 84, s='*Rayno Popovich', rotation=0, family='sans-serif', size=10)
plt.text(161, 97, s='*Billa 1', rotation=0, family='sans-serif', size=10)
plt.text(140, 97, s='*L.Karavelov School', rotation=35, family='sans-serif', size=10)
plt.text(91, 65, s='Shahbazyan Sq*', rotation=35, family='sans-serif', size=10)
plt.text(32, 81, s='*Nedelya', rotation=35, family='sans-serif', size=10)
plt.text(-20.5, 82, s='*N.Mushanov Sq', rotation=35, family='sans-serif', size=10)
plt.text(160, 46, s='*Bratya Sveshtarovi', rotation=0, family='sans-serif', size=10)
plt.text(160, 14, s='*Botev Stadium', rotation=0, family='sans-serif', size=10)
plt.text(-51.5, 94, s='Skoda*', rotation=0, family='sans-serif', size=10)
plt.text(-51.5, 44, s='Medical Centre*', rotation=35, family='sans-serif', size=10)
plt.text(-10, 53.5, s='Flamingo*', rotation=35, family='sans-serif', size=10)
plt.text(21, 55, s='Bunardzhika*', rotation=35, family='sans-serif', size=10)
plt.text(22, 28, s='Markovo Tepe*', rotation=0, family='sans-serif', size=10)
plt.text(71, -7, s='*South Bus Station', rotation=35, family='sans-serif', size=10)
plt.text(83, -24, s='Stochna Railway*\nStation', rotation=35, family='sans-serif', size=10)
plt.text(109, -22, s='Medical Academy*', rotation=35, family='sans-serif', size=10)
plt.text(162, -6, s='*Agricultural University', rotation=0, family='sans-serif', size=10)
plt.text(69, 81, s='*Saedinenie Sq', rotation=0, family='sans-serif', size=10)
#Display description of the map
plt.text(
    190, -37,
    s='-|- City of Plovdiv -|-\nPublic Transport Map (Bus Lines:99,7,93,9) ',
    color= '#696969',
    weight= 'bold',
    verticalalignment='bottom',
    horizontalalignment='center',
    rotation=0,
    family='sans-serif',
    size=10)
# Draw the nodes as well as hiding the original labels off the nodes
nx.draw_networkx(
    MyGraph, pos,
    node_color=NodeList,
    font_size=0,
)
# Draw the edges
nx.draw_networkx_edges(MyGraph, pos, edge_color=EdgeList)
# Draw new labels on the nodes in order to give it more attributes (resize and make it more readable)
nx.draw_networkx_labels(
    MyGraph, pos,
    labels=None,
    font_size=8,
    font_color='#000000',
    font_family='sans-serif',
    font_weight='bold',
    alpha=None,
    bbox=None,
    horizontalalignment='center',
    verticalalignment='center',
    ax=None,
    clip_on=None
)
# Draw the labels on the edges (distance)
nx.draw_networkx_edge_labels(
    MyGraph, pos,
    edge_labels={
                # Green Line Distance
                 ('B7', 'C7'): '0,2 km',
                 ('C7', 'D7'): '0,4 km',
                 ('D7', 'E7'): '0,2 km',
                 ('E7', 'F7'): '0,5 km',
                 ('F7', 'G7'): '0,8 km',
                 ('G7', 'H7'): '1,2 km',
                # Blue Line Distance
                 ('B99', 'C99'): '0,4 km',
                 ('C99', 'D99'): '0,4 km',
                 ('D99', 'E99'): '0,4 km',
                 ('E99', 'F99'): '0,3 km',
                 ('F99', 'G99'): '0,2 km',
                 ('G99', 'H99'): '0,65 km',
                 ('H99', 'I99'): '0,2 km',
                 ('I99', 'J99'): '0,4 km',
                 ('J99', 'K99'): '0,4 km',
                 ('K99', 'L99'): '0,6 km',
                 ('L99', 'M99'): '0,45 km',
                 ('M99', 'N99'): '0,7 km',
                # ORANGE LINE DISTANCE
                ('N93', 'M93'): '0,4 km',
                ('M93', 'L93'): '0,4 km',
                ('L93', 'K93'): '0,4 km',
                ('K93', 'J93'): '0,3 km',
                ('J93', 'I93'): '0,45 km',
                ('I93', 'H93'): '0,65 km',
                ('H93', 'G93'): '0,25 km',
                ('G93', 'F93'): '0,4 km',
                ('F93', 'E93'): '0,3 km',
                ('E93', 'D93'): '0,3 km',
                ('D93', 'C93'): '0,3 km',
                ('C93', 'B93'): '0,45 km',
                # YELLOW LINE DISTANCE
                ('B9', 'C9'): '0,65 km',
                ('C9', 'D9'): '0,25 km',
                ('D9', 'E9'): '0,4 km',
                ('E9', 'F9'): '0,28 km',
                ('F9', 'G9'): '0,3 km',
                ('G9', 'H9'): '0,3 km',
                ('H9', 'I9'): '0,55 km',
                ('I9', 'J9'): '0,6 km',
                ('J9', 'K9'): '0,4 km',
                 },
    font_color='red',
    font_size='5.5',
    font_family='sans',
    font_weight='bold'
)
# Visualise the graph
plt.show()
