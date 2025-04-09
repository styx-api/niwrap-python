# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PULSE_METADATA = Metadata(
    id="58a6304ff6bc7912186d579f3a1f6543eccbc5c5.boutiques",
    name="pulse",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


PulseParameters = typing.TypedDict('PulseParameters', {
    "__STYX_TYPE__": typing.Literal["pulse"],
    "input_file": InputPathType,
    "output_base": str,
    "seq": typing.NotRequired[str | None],
    "angle": typing.NotRequired[float | None],
    "te": typing.NotRequired[float | None],
    "tr": typing.NotRequired[float | None],
    "trslc": typing.NotRequired[float | None],
    "nx": typing.NotRequired[float | None],
    "ny": typing.NotRequired[float | None],
    "dx": typing.NotRequired[float | None],
    "dy": typing.NotRequired[float | None],
    "maxG": typing.NotRequired[float | None],
    "riset": typing.NotRequired[float | None],
    "bw": typing.NotRequired[float | None],
    "numvol": typing.NotRequired[float | None],
    "numslc": typing.NotRequired[float | None],
    "slcthk": typing.NotRequired[float | None],
    "gap": typing.NotRequired[float | None],
    "zstart": typing.NotRequired[float | None],
    "slcdir": typing.NotRequired[str | None],
    "phasedir": typing.NotRequired[str | None],
    "readdir": typing.NotRequired[str | None],
    "verbose_flag": bool,
    "kcoord_flag": bool,
    "cover": typing.NotRequired[float | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "pulse": pulse_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "pulse": pulse_outputs,
    }.get(t)


class PulseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `pulse(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_pulse_sequence_matrix: OutputPathType
    """Pulse sequence matrix output"""


def pulse_params(
    input_file: InputPathType,
    output_base: str,
    seq: str | None = "epi",
    angle: float | None = 90,
    te: float | None = 0.03,
    tr: float | None = 3,
    trslc: float | None = 0.12,
    nx: float | None = 64,
    ny: float | None = 64,
    dx: float | None = 0.004,
    dy: float | None = 0.004,
    max_g: float | None = 0.055,
    riset: float | None = 0.00022,
    bw: float | None = 100000,
    numvol: float | None = 1,
    numslc: float | None = 1,
    slcthk: float | None = 0.006,
    gap: float | None = 0,
    zstart: float | None = 0,
    slcdir: str | None = "z-",
    phasedir: str | None = "y+",
    readdir: str | None = "x+",
    verbose_flag: bool = False,
    kcoord_flag: bool = False,
    cover: float | None = None,
) -> PulseParameters:
    """
    Build parameters.
    
    Args:
        input_file: 4D digital brain, resolution can be any.
        output_base: Output base name.
        seq: Type of pulse sequence; default=epi (epi OR ge).
        angle: Flip angle in degrees; default=90.
        te: The time from the first RF to the first echo; default=0.03s.
        tr: The time between the two RF pulses applied on the same part of the\
            object; default=3s.
        trslc: The time that takes for the acquisition of one slice;\
            default=0.12s.
        nx: Resolution in x of the output image; default=64.
        ny: Resolution in y of the output image; default=64.
        dx: Image voxel x-dimension; default=0.004m.
        dy: Image voxel y-dimension; default=0.004m.
        max_g: Maximum gradient strength; default=0.055 T/m.
        riset: Time it takes for the gradient to reach its max value;\
            default=0.00022s.
        bw: Receiving bandwidth; default=100000Hz.
        numvol: Number of volumes; default=1.
        numslc: Number of slices; default=1.
        slcthk: Slice thickness; default=0.006m.
        gap: Gap between the slices in meters; default=0m.
        zstart: The lowest position in the slice direction in meters;\
            default=0m.
        slcdir: Slice acquisition direction/orientation; default=z- (x+,x-,\
            y+,y- or z+,or z-).
        phasedir: Phase encode direction/orientation; default=y+ (x+,x-, y+,y-\
            or z+,or z-).
        readdir: Read-out direction/orientation; default=x+ (x+,x-, y+,y- or\
            z+,or z-).
        verbose_flag: Switch on diagnostic messages.
        kcoord_flag: Save k-space coordinates; default=no.
        cover: Phase partial Fourier coverage in percentage; default=100\
            (min=50, max=100).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "pulse",
        "input_file": input_file,
        "output_base": output_base,
        "verbose_flag": verbose_flag,
        "kcoord_flag": kcoord_flag,
    }
    if seq is not None:
        params["seq"] = seq
    if angle is not None:
        params["angle"] = angle
    if te is not None:
        params["te"] = te
    if tr is not None:
        params["tr"] = tr
    if trslc is not None:
        params["trslc"] = trslc
    if nx is not None:
        params["nx"] = nx
    if ny is not None:
        params["ny"] = ny
    if dx is not None:
        params["dx"] = dx
    if dy is not None:
        params["dy"] = dy
    if max_g is not None:
        params["maxG"] = max_g
    if riset is not None:
        params["riset"] = riset
    if bw is not None:
        params["bw"] = bw
    if numvol is not None:
        params["numvol"] = numvol
    if numslc is not None:
        params["numslc"] = numslc
    if slcthk is not None:
        params["slcthk"] = slcthk
    if gap is not None:
        params["gap"] = gap
    if zstart is not None:
        params["zstart"] = zstart
    if slcdir is not None:
        params["slcdir"] = slcdir
    if phasedir is not None:
        params["phasedir"] = phasedir
    if readdir is not None:
        params["readdir"] = readdir
    if cover is not None:
        params["cover"] = cover
    return params


def pulse_cargs(
    params: PulseParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("pulse")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-o",
        params.get("output_base")
    ])
    if params.get("seq") is not None:
        cargs.extend([
            "--seq",
            params.get("seq")
        ])
    if params.get("angle") is not None:
        cargs.extend([
            "--angle",
            str(params.get("angle"))
        ])
    if params.get("te") is not None:
        cargs.extend([
            "--te",
            str(params.get("te"))
        ])
    if params.get("tr") is not None:
        cargs.extend([
            "--tr",
            str(params.get("tr"))
        ])
    if params.get("trslc") is not None:
        cargs.extend([
            "--trslc",
            str(params.get("trslc"))
        ])
    if params.get("nx") is not None:
        cargs.extend([
            "--nx",
            str(params.get("nx"))
        ])
    if params.get("ny") is not None:
        cargs.extend([
            "--ny",
            str(params.get("ny"))
        ])
    if params.get("dx") is not None:
        cargs.extend([
            "--dx",
            str(params.get("dx"))
        ])
    if params.get("dy") is not None:
        cargs.extend([
            "--dy",
            str(params.get("dy"))
        ])
    if params.get("maxG") is not None:
        cargs.extend([
            "--maxG",
            str(params.get("maxG"))
        ])
    if params.get("riset") is not None:
        cargs.extend([
            "--riset",
            str(params.get("riset"))
        ])
    if params.get("bw") is not None:
        cargs.extend([
            "--bw",
            str(params.get("bw"))
        ])
    if params.get("numvol") is not None:
        cargs.extend([
            "--numvol",
            str(params.get("numvol"))
        ])
    if params.get("numslc") is not None:
        cargs.extend([
            "--numslc",
            str(params.get("numslc"))
        ])
    if params.get("slcthk") is not None:
        cargs.extend([
            "--slcthk",
            str(params.get("slcthk"))
        ])
    if params.get("gap") is not None:
        cargs.extend([
            "--gap",
            str(params.get("gap"))
        ])
    if params.get("zstart") is not None:
        cargs.extend([
            "--zstart",
            str(params.get("zstart"))
        ])
    if params.get("slcdir") is not None:
        cargs.extend([
            "--slcdir",
            params.get("slcdir")
        ])
    if params.get("phasedir") is not None:
        cargs.extend([
            "--phasedir",
            params.get("phasedir")
        ])
    if params.get("readdir") is not None:
        cargs.extend([
            "--readdir",
            params.get("readdir")
        ])
    if params.get("verbose_flag"):
        cargs.append("-v")
    if params.get("kcoord_flag"):
        cargs.append("-k")
    if params.get("cover") is not None:
        cargs.extend([
            "--cover",
            str(params.get("cover"))
        ])
    return cargs


def pulse_outputs(
    params: PulseParameters,
    execution: Execution,
) -> PulseOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PulseOutputs(
        root=execution.output_file("."),
        output_pulse_sequence_matrix=execution.output_file(params.get("output_base") + "_pulsesequence_matrix"),
    )
    return ret


def pulse_execute(
    params: PulseParameters,
    execution: Execution,
) -> PulseOutputs:
    """
    Generates a pulse sequence matrix for a given digital brain image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PulseOutputs`).
    """
    params = execution.params(params)
    cargs = pulse_cargs(params, execution)
    ret = pulse_outputs(params, execution)
    execution.run(cargs)
    return ret


def pulse(
    input_file: InputPathType,
    output_base: str,
    seq: str | None = "epi",
    angle: float | None = 90,
    te: float | None = 0.03,
    tr: float | None = 3,
    trslc: float | None = 0.12,
    nx: float | None = 64,
    ny: float | None = 64,
    dx: float | None = 0.004,
    dy: float | None = 0.004,
    max_g: float | None = 0.055,
    riset: float | None = 0.00022,
    bw: float | None = 100000,
    numvol: float | None = 1,
    numslc: float | None = 1,
    slcthk: float | None = 0.006,
    gap: float | None = 0,
    zstart: float | None = 0,
    slcdir: str | None = "z-",
    phasedir: str | None = "y+",
    readdir: str | None = "x+",
    verbose_flag: bool = False,
    kcoord_flag: bool = False,
    cover: float | None = None,
    runner: Runner | None = None,
) -> PulseOutputs:
    """
    Generates a pulse sequence matrix for a given digital brain image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: 4D digital brain, resolution can be any.
        output_base: Output base name.
        seq: Type of pulse sequence; default=epi (epi OR ge).
        angle: Flip angle in degrees; default=90.
        te: The time from the first RF to the first echo; default=0.03s.
        tr: The time between the two RF pulses applied on the same part of the\
            object; default=3s.
        trslc: The time that takes for the acquisition of one slice;\
            default=0.12s.
        nx: Resolution in x of the output image; default=64.
        ny: Resolution in y of the output image; default=64.
        dx: Image voxel x-dimension; default=0.004m.
        dy: Image voxel y-dimension; default=0.004m.
        max_g: Maximum gradient strength; default=0.055 T/m.
        riset: Time it takes for the gradient to reach its max value;\
            default=0.00022s.
        bw: Receiving bandwidth; default=100000Hz.
        numvol: Number of volumes; default=1.
        numslc: Number of slices; default=1.
        slcthk: Slice thickness; default=0.006m.
        gap: Gap between the slices in meters; default=0m.
        zstart: The lowest position in the slice direction in meters;\
            default=0m.
        slcdir: Slice acquisition direction/orientation; default=z- (x+,x-,\
            y+,y- or z+,or z-).
        phasedir: Phase encode direction/orientation; default=y+ (x+,x-, y+,y-\
            or z+,or z-).
        readdir: Read-out direction/orientation; default=x+ (x+,x-, y+,y- or\
            z+,or z-).
        verbose_flag: Switch on diagnostic messages.
        kcoord_flag: Save k-space coordinates; default=no.
        cover: Phase partial Fourier coverage in percentage; default=100\
            (min=50, max=100).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PulseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PULSE_METADATA)
    params = pulse_params(
        input_file=input_file,
        output_base=output_base,
        seq=seq,
        angle=angle,
        te=te,
        tr=tr,
        trslc=trslc,
        nx=nx,
        ny=ny,
        dx=dx,
        dy=dy,
        max_g=max_g,
        riset=riset,
        bw=bw,
        numvol=numvol,
        numslc=numslc,
        slcthk=slcthk,
        gap=gap,
        zstart=zstart,
        slcdir=slcdir,
        phasedir=phasedir,
        readdir=readdir,
        verbose_flag=verbose_flag,
        kcoord_flag=kcoord_flag,
        cover=cover,
    )
    return pulse_execute(params, execution)


__all__ = [
    "PULSE_METADATA",
    "PulseOutputs",
    "PulseParameters",
    "pulse",
    "pulse_params",
]
