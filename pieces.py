#!/usr/bin/env python

# kristen widman
# Oct 22, 2012

from messages import *

class Block(object):
    def __init__(self, expected_length, bytestring=''):
        '''expected length should be an int'''
        self.bytestring = bytestring
        #print 'actual length of string: ' + str(len(bytestring))
        #print 'block length expected  :  ' + str(expected_length)
        if len(self.bytestring) == expected_length:
            self.full = True
            #print True
        else:
            self.full = False
            #print False

    def __repr__(self):
        #if self.bytestring == '':
            #return 'None'
        #else:
            return repr(self.bytestring)

class Piece(object):
    def __init__(self, piece_size):
        #self.block_size = 2**14
        self.block_size = 2**3
        block_number = piece_size/self.block_size
        self.block_list = []
        for block in range(block_number):
            self.block_list.append(Block(self.block_size))
        #self.block_list = [Block(self.block_size) * block_number]  #will this work?
        if piece_size % self.block_size != 0:
            print 'extra block for this piece'
            block_size_last = piece_size % self.block_size
            self.block_list.append(Block(block_size_last))
        #print 'block number ' + str(len(self.block_list))
        #print 'initial block_list ' + repr(self.block_list)
        self.full = self.check_if_full()  #There's probably a more elegant way to write this -- use 'all'?
        print 'piece is full? ' + str(self.full)

    def check_if_full(self):
        full = True
        for block in self.block_list:
            if block.full == False:
                full = False
        return full

    def write_block(self, piece_offset, bytestring):
        block_index = piece_offset / self.block_size
        #print 'in write_block, piece offset is ' + str(piece_offset) + ' and block size is ' + str(self.block_size)
        print 'block_index is ' + str(block_index)
        self.block_list[block_index].bytestring = bytestring

    def return_block(self, piece_offset):
        block_index = piece_offset / self.block_size
        return self.block_list[block_index].bytestring
    
    def __repr__(self):
        to_print = ''.join(repr(block) for block in self.block_list)
        return to_print

if __name__ == "__main__":
    print 'testing blocks and pieces'
    block = Block(bytes_to_number('\x00\x00\x06\x18'),'\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9d\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff')
    #print 'block: ' + repr(block)
    #piece = Piece(1048576)
    piece = Piece(2**3 * 10+4)
    piece.write_block(bytes_to_number('\x00\x00\x00\x41'), '\x01\x01\x01\x01\x05\x01\x01\x09')
    print repr(piece)