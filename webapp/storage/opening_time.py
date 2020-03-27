# encoding: utf-8

"""
Copyright (c) 2017, Ernesto Ruge
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from math import floor
from ..extensions import db
from .base import BaseModel


class OpeningTime(db.Model, BaseModel):
    __tablename__ = 'opening_time'

    version = '0.9.0'

    fields = [
        'id', 'created', 'modified', 'store_id', 'type', 'weekday', 'open', 'close'
    ]

    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))

    type = db.Column(db.Enum('all', 'delivery', 'counter', 'pickup'))
    weekday = db.Column(db.Integer)
    open = db.Column(db.Integer)
    close = db.Column(db.Integer)

    @property
    def weekday_out(self):
        if self.weekday == 1:
            return 'Montag'
        if self.weekday == 2:
            return 'Dienstag'
        if self.weekday == 3:
            return 'Mittwoch'
        if self.weekday == 4:
            return 'Donnerstag'
        if self.weekday == 5:
            return 'Freitag'
        if self.weekday == 6:
            return 'Samstag'
        if self.weekday == 7:
            return 'Sonntag'

    @property
    def open_out(self):
        return self.decode_time(self.open)

    @property
    def close_out(self):
        return self.decode_time(self.close)

    def decode_time(self, t):
        if not t:
            return ''
        return '%02d:%02d' % (floor(t / 3600), (t / 60) % 60)
