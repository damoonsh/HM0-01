<h1 align="center">HM0-01: Platform for training a maze solver </h1>

<p align="center">
  <img src="/img/entry_point.png" width=80% height=80% alt="Demo"/>
</p>

- ```Testing the basic functionality.```
- ```Choose between user/computer mode.```
- ```Choose the dimensions of the map.```

<h5> Platform variables: </h5>

- `x`: Pauses the movement.
- `space`: Resets the map.
- `r`: resets the map and the object.

# This project has two partitions:
Partition 01: Computer| Partition 02: The **self-learning** side
---------------------------- | ----------------------------
Generates a random maze with graphics | Travels through the maze and tries to optimize it's movement by gathering data about the map.
Monitors the movements of the second partion. | It stores the data it has collected and makes its dicisions based on the previous trials
Acts as an supervisor to the second partion but does not interfere | Acts as the learner and it gets smarter in a way to optimize it's path.

<br />

### Partion 01: 
By the use of the modules in Map, Consts  and the utilties in the  utility folder, there is a map generated.
      Markup : <details>
                 <summary>Map</summary>
                 <p align="center">
                  In this module, there is a 2D array of <b>0's</b> and <b>1's</b> produced and based on this array 
                  the gets generated. 
                 </p>
               </details>
               <details>
                 <summary>Utilities</summary>
                 <p align="center">
                  In this directory, there are constant variables and as well as some loggings that are stored to 
                  help the user interact with the platform.
                 </p>
               </details>

### Partion 02:
<p align="left">
  They are two main aspects to the mover module(which controls the self-learning partition.). The first one is that
  it goes through the map and records its own moves and mistakes(when it ends up in a deadend). The second part is where it     decides what to do based on the previously collected data, in other words by doing analysis on the data, it tries to avoid
  making the old mistakes and in other words, it learns.
</p>

The schema for stored data:
```
path_info = {
  "coor": (self.x, self.y),
  "options": [d for d in dirs if self.possible_moves[d] and not (d in self.visited)],
  "move_type": [dir]
}
```

<h6> Which can be visualised as: </h6>
<p align="center">
  <img src="/img/demo.png" width=90% height=90% alt="Demo" />
</p>
