"""
    py-faster-rcnn-ft - Custom Training of Deep Learning Models for Image Classification
    Copyright (C) 2017  DFKI GmbH

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from google.protobuf import text_format
import caffe.proto.caffe_pb2 as caffe_pb2
import os


class PrototxtManager:
    """A PrototxtManager loads a prototxt file from the disc and allows to perform manipulations on the file"""

    def __init__(self, filename):

        self.filename = filename
        self.net = caffe_pb2.NetParameter()

        # check if file exists
        if not os.path.isfile(filename):
            print "the file {} does not exist".format(filename)
            assert False

        # check if file is .prototxt
        if not filename.endswith('.prototxt'):
            print "the file {} must be a .prototxt file".format(filename)
            assert False

        # write the content of the protoxt file into self.net
        with open(filename, 'r') as f:
            text_format.Merge(f.read(), self.net)

    def get_layer_by_index(self, index):
        return self.net.layer[index]

    def get_layer_by_name(self, layer_name):

        for cur_layer in self.net.layer:
            if cur_layer.name == layer_name:
                return cur_layer

    def write_prototxt(self, output_filename):
        with open(output_filename, 'w') as outf:
            outf.write(str(self.net))

    def set_net_name(self, new_name, postfix=True):

        if postfix:
            self.net.name += "_" + new_name
