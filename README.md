# fumadores

El link de este repositorio es el siguiente: [GitHub](https://github.com/joseluis031/fumadores.git)

## Se resuelve el siguiente problema

El caso de los fumadores consiste en un grupo de fumadores que para fumar necesitan los ingredientes que les faltan para hacer un cigarrillo y fumárselo, poseen un ingrediente en cantidades ilimitadas pero les faltan otros cuatro.

El agente posee cantidades ilimitadas de todos los ingredientes que son papel, tabaco, filtros, green y cerillas pero solo deja en una mesa dos de estos ingredientes a la vez. Cada fumador posee un ingrediente distinto de los cinco necesarios y según los ingredientes que deje el agente uno de los fumadores podrá fumar con los cuatro ingredientes que el agente deja.

El agente y los fumadores representan en la realidad a procesos y los ingredientes a los recursos de un sistema. La dificultad radica en sincronizar los agentes y fumadores para que el agente cuando deje ingredientes en la mesa el fumador correcto fume.

A primera vista podríamos intentar que cada uno de los fumadores tomase cada uno de los ingredientes que le falta y se pusiese a fumar representando un ingrediente como un semáforo, sin embargo, esta solución puede producir un bloqueo si uno de los otros fumadores que no pueden fumar según los ingredientes que ha dejado el agente le quitan al que podría fumar uno de los ingredientes que necesita. Por ejemplo, un caso de bloqueo sería el caso de que el agente deje en la mesa los ingredientes de tabaco y cerillas el fumador que podría fumar sería el 1 pero si el fumador 2 es más rápido y se ejecuta antes tomando el tabaco el fumador 1 se quedaría esperando a tomar tabaco y el fumador 2 también por no haber dejado el agente papel sino cerillas.
