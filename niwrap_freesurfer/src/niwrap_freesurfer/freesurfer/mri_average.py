# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_AVERAGE_METADATA = Metadata(
    id="eb15546d738076b6fe7c57e66238b82613f7eb29.boutiques",
    name="mri_average",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriAverageParameters = typing.TypedDict('MriAverageParameters', {
    "__STYX_TYPE__": typing.Literal["mri_average"],
    "input_volumes": list[InputPathType],
    "output_volume": str,
    "rigid_alignment": bool,
    "read_from_file": bool,
    "dt": typing.NotRequired[float | None],
    "tol": typing.NotRequired[float | None],
    "conform": bool,
    "noconform": bool,
    "reduce": typing.NotRequired[float | None],
    "sinc_interpolation": typing.NotRequired[float | None],
    "trilinear": bool,
    "window": bool,
    "snapshots": typing.NotRequired[float | None],
    "translation": typing.NotRequired[list[float] | None],
    "rotation": typing.NotRequired[list[float] | None],
    "momentum": typing.NotRequired[float | None],
    "rms": bool,
    "rms_alt": bool,
    "percent": bool,
    "binarize": typing.NotRequired[float | None],
    "absolute": bool,
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
        "mri_average": mri_average_cargs,
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
        "mri_average": mri_average_outputs,
    }.get(t)


class MriAverageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_average(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """The averaged output volume."""


def mri_average_params(
    input_volumes: list[InputPathType],
    output_volume: str,
    rigid_alignment: bool = False,
    read_from_file: bool = False,
    dt: float | None = None,
    tol: float | None = None,
    conform: bool = False,
    noconform: bool = False,
    reduce: float | None = None,
    sinc_interpolation: float | None = None,
    trilinear: bool = False,
    window: bool = False,
    snapshots: float | None = None,
    translation: list[float] | None = None,
    rotation: list[float] | None = None,
    momentum: float | None = None,
    rms: bool = False,
    rms_alt: bool = False,
    percent: bool = False,
    binarize: float | None = None,
    absolute: bool = False,
) -> MriAverageParameters:
    """
    Build parameters.
    
    Args:
        input_volumes: Input volumes to average.
        output_volume: Output volume file.
        rigid_alignment: Rigid alignment of input volumes before averaging.
        read_from_file: Read volumes from an input file (first argument is the\
            input filename).
        dt: Set dt to n (default=1e-6).
        tol: Set tolerance to n (default=1e-5).
        conform: Interpolate volume to be isotropic 1mm^3 (on by default).
        noconform: Inhibit isotropic volume interpolation.
        reduce: Reduce input images n (default=2) times.
        sinc_interpolation: Using sinc interpolation with window width of 2*n\
            (default=3).
        trilinear: Use trilinear interpolation.
        window: Apply hanning window to volumes.
        snapshots: Write snapshots every n iterations.
        translation: Translation of second volume.
        rotation: Rotation of second volume around each axis in degrees.
        momentum: Use momentum n (default=0).
        rms: Compute sqrt of average of sum of squares (RMS, same as -rms).
        rms_alt: Compute sqrt of average of sum of squares (RMS, same as -sqr).
        percent: Compute percentage.
        binarize: Binarize the input volumes using threshold th.
        absolute: Take absolute value of volume.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_average",
        "input_volumes": input_volumes,
        "output_volume": output_volume,
        "rigid_alignment": rigid_alignment,
        "read_from_file": read_from_file,
        "conform": conform,
        "noconform": noconform,
        "trilinear": trilinear,
        "window": window,
        "rms": rms,
        "rms_alt": rms_alt,
        "percent": percent,
        "absolute": absolute,
    }
    if dt is not None:
        params["dt"] = dt
    if tol is not None:
        params["tol"] = tol
    if reduce is not None:
        params["reduce"] = reduce
    if sinc_interpolation is not None:
        params["sinc_interpolation"] = sinc_interpolation
    if snapshots is not None:
        params["snapshots"] = snapshots
    if translation is not None:
        params["translation"] = translation
    if rotation is not None:
        params["rotation"] = rotation
    if momentum is not None:
        params["momentum"] = momentum
    if binarize is not None:
        params["binarize"] = binarize
    return params


def mri_average_cargs(
    params: MriAverageParameters,
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
    cargs.append("mri_average")
    cargs.extend([execution.input_file(f) for f in params.get("input_volumes")])
    cargs.append(params.get("output_volume"))
    if params.get("rigid_alignment"):
        cargs.append("-a")
    if params.get("read_from_file"):
        cargs.append("-F")
    if params.get("dt") is not None:
        cargs.extend([
            "-dt",
            str(params.get("dt"))
        ])
    if params.get("tol") is not None:
        cargs.extend([
            "-tol",
            str(params.get("tol"))
        ])
    if params.get("conform"):
        cargs.append("-conform")
    if params.get("noconform"):
        cargs.append("-noconform")
    if params.get("reduce") is not None:
        cargs.extend([
            "-reduce",
            str(params.get("reduce"))
        ])
    if params.get("sinc_interpolation") is not None:
        cargs.extend([
            "-sinc",
            str(params.get("sinc_interpolation"))
        ])
    if params.get("trilinear"):
        cargs.append("-trilinear")
    if params.get("window"):
        cargs.append("-window")
    if params.get("snapshots") is not None:
        cargs.extend([
            "-w",
            str(params.get("snapshots"))
        ])
    if params.get("translation") is not None:
        cargs.extend([
            "-t",
            *map(str, params.get("translation"))
        ])
    if params.get("rotation") is not None:
        cargs.extend([
            "-r",
            *map(str, params.get("rotation"))
        ])
    if params.get("momentum") is not None:
        cargs.extend([
            "-m",
            str(params.get("momentum"))
        ])
    if params.get("rms"):
        cargs.append("-sqr")
    if params.get("rms_alt"):
        cargs.append("-rms")
    if params.get("percent"):
        cargs.append("-p")
    if params.get("binarize") is not None:
        cargs.extend([
            "-b",
            str(params.get("binarize"))
        ])
    if params.get("absolute"):
        cargs.append("-abs")
    return cargs


def mri_average_outputs(
    params: MriAverageParameters,
    execution: Execution,
) -> MriAverageOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriAverageOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_average_execute(
    params: MriAverageParameters,
    execution: Execution,
) -> MriAverageOutputs:
    """
    Averages multiple volumes with various options for alignment, interpolation, and
    transformations.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriAverageOutputs`).
    """
    params = execution.params(params)
    cargs = mri_average_cargs(params, execution)
    ret = mri_average_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_average(
    input_volumes: list[InputPathType],
    output_volume: str,
    rigid_alignment: bool = False,
    read_from_file: bool = False,
    dt: float | None = None,
    tol: float | None = None,
    conform: bool = False,
    noconform: bool = False,
    reduce: float | None = None,
    sinc_interpolation: float | None = None,
    trilinear: bool = False,
    window: bool = False,
    snapshots: float | None = None,
    translation: list[float] | None = None,
    rotation: list[float] | None = None,
    momentum: float | None = None,
    rms: bool = False,
    rms_alt: bool = False,
    percent: bool = False,
    binarize: float | None = None,
    absolute: bool = False,
    runner: Runner | None = None,
) -> MriAverageOutputs:
    """
    Averages multiple volumes with various options for alignment, interpolation, and
    transformations.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volumes: Input volumes to average.
        output_volume: Output volume file.
        rigid_alignment: Rigid alignment of input volumes before averaging.
        read_from_file: Read volumes from an input file (first argument is the\
            input filename).
        dt: Set dt to n (default=1e-6).
        tol: Set tolerance to n (default=1e-5).
        conform: Interpolate volume to be isotropic 1mm^3 (on by default).
        noconform: Inhibit isotropic volume interpolation.
        reduce: Reduce input images n (default=2) times.
        sinc_interpolation: Using sinc interpolation with window width of 2*n\
            (default=3).
        trilinear: Use trilinear interpolation.
        window: Apply hanning window to volumes.
        snapshots: Write snapshots every n iterations.
        translation: Translation of second volume.
        rotation: Rotation of second volume around each axis in degrees.
        momentum: Use momentum n (default=0).
        rms: Compute sqrt of average of sum of squares (RMS, same as -rms).
        rms_alt: Compute sqrt of average of sum of squares (RMS, same as -sqr).
        percent: Compute percentage.
        binarize: Binarize the input volumes using threshold th.
        absolute: Take absolute value of volume.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriAverageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_AVERAGE_METADATA)
    params = mri_average_params(
        input_volumes=input_volumes,
        output_volume=output_volume,
        rigid_alignment=rigid_alignment,
        read_from_file=read_from_file,
        dt=dt,
        tol=tol,
        conform=conform,
        noconform=noconform,
        reduce=reduce,
        sinc_interpolation=sinc_interpolation,
        trilinear=trilinear,
        window=window,
        snapshots=snapshots,
        translation=translation,
        rotation=rotation,
        momentum=momentum,
        rms=rms,
        rms_alt=rms_alt,
        percent=percent,
        binarize=binarize,
        absolute=absolute,
    )
    return mri_average_execute(params, execution)


__all__ = [
    "MRI_AVERAGE_METADATA",
    "MriAverageOutputs",
    "MriAverageParameters",
    "mri_average",
    "mri_average_params",
]
