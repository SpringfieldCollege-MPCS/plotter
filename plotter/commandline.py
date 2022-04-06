import argparse
from ast import parse
from plotter import plotter

def parse_args():
    parser = argparse.ArgumentParser(description="Plots numbers")
    parser.add_argument("-x", nargs="+", help="All your x arguments")
    parser.add_argument("-y", nargs="+", help="All your y arguments")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    plotter(args.x, args.y)
