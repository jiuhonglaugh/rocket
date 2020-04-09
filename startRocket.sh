#!/bin/bash
ROCKET_HOME=$(cd `dirname $0`; pwd)
ROCKET_PID=$ROCKET_HOME/run/rocket.pid

function start(){
	echo -e "= = = = = = = = = = = = = Start $1 = = = = = = = = = = = = =\n"
	names=$(getStat $1)
	if [[ $names == *$1* ]];then
		echo "$1 IS RUNNING"
	else
		$1$COMMOND start
	fi
}

function getStat(){
	if [ -f $ROCKET_PID ];then
		pid=`cat ROCKET_PID`
		pid=`jps | grep $pid | awk '{print $1}'`
		[ ! -z $pid ] && echo -n $1
	fi
}

nohup python3 $ROCKET_HOME/main.py >> $ROCKET_HOME/logs/rocket.log 2>&1 &
echo $! > $ROCKET_HOME/run/rocket.pid
