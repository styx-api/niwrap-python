# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_INTENSITY_PROFILE_METADATA = Metadata(
    id="beda2c859ac2d0a2d1258f38cd59663f80ffddd8.boutiques",
    name="mris_intensity_profile",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisIntensityProfileParameters = typing.TypedDict('MrisIntensityProfileParameters', {
    "__STYXTYPE__": typing.Literal["mris_intensity_profile"],
    "subject_name": str,
    "hemi": str,
    "volume": InputPathType,
    "output_file": str,
    "write_surf": typing.NotRequired[str | None],
    "sdir": typing.NotRequired[str | None],
    "white": typing.NotRequired[str | None],
    "pial": typing.NotRequired[str | None],
    "normalize_flag": bool,
    "mean": typing.NotRequired[str | None],
    "xform": typing.NotRequired[InputPathType | None],
    "src": typing.NotRequired[InputPathType | None],
    "dst": typing.NotRequired[InputPathType | None],
    "invert_flag": bool,
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
        "mris_intensity_profile": mris_intensity_profile_cargs,
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
        "mris_intensity_profile": mris_intensity_profile_outputs,
    }.get(t)


class MrisIntensityProfileOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_intensity_profile(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_curvature_file: OutputPathType
    """Curvature file with the intensity profile measurement."""
    output_mean_profile_integral: OutputPathType | None
    """File with the mean profile-integral."""


def mris_intensity_profile_params(
    subject_name: str,
    hemi: str,
    volume: InputPathType,
    output_file: str,
    write_surf: str | None = None,
    sdir: str | None = None,
    white: str | None = None,
    pial: str | None = None,
    normalize_flag: bool = False,
    mean: str | None = None,
    xform: InputPathType | None = None,
    src: InputPathType | None = None,
    dst: InputPathType | None = None,
    invert_flag: bool = False,
) -> MrisIntensityProfileParameters:
    """
    Build parameters.
    
    Args:
        subject_name: Name of the subject.
        hemi: Hemisphere (e.g. lh or rh).
        volume: Volume file to be processed.
        output_file: Output file where the measurement is saved.
        write_surf: Write the variational pial surface target locations.
        sdir: Specifies the SUBJECTS_DIR.
        white: Specifies the WHITE surface filename.
        pial: Specifies the PIAL surface filename.
        normalize_flag: Normalized sampling with respect to thickness.
        mean: Outputs the mean profile-integral to the specified file (output\
            is in curv format).
        xform: Specify the registration transformation that maps the T1 volume\
            to the input volume to be sampled.
        src: Source volume used when computing the registration transformation.
        dst: Destination volume used when computing the registration\
            transformation.
        invert_flag: Apply the registration transformation inversely.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_intensity_profile",
        "subject_name": subject_name,
        "hemi": hemi,
        "volume": volume,
        "output_file": output_file,
        "normalize_flag": normalize_flag,
        "invert_flag": invert_flag,
    }
    if write_surf is not None:
        params["write_surf"] = write_surf
    if sdir is not None:
        params["sdir"] = sdir
    if white is not None:
        params["white"] = white
    if pial is not None:
        params["pial"] = pial
    if mean is not None:
        params["mean"] = mean
    if xform is not None:
        params["xform"] = xform
    if src is not None:
        params["src"] = src
    if dst is not None:
        params["dst"] = dst
    return params


def mris_intensity_profile_cargs(
    params: MrisIntensityProfileParameters,
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
    cargs.append("mris_intensity_profile")
    cargs.append(params.get("subject_name"))
    cargs.append(params.get("hemi"))
    cargs.append(execution.input_file(params.get("volume")))
    cargs.append(params.get("output_file"))
    if params.get("write_surf") is not None:
        cargs.extend([
            "-write_surf",
            params.get("write_surf")
        ])
    if params.get("sdir") is not None:
        cargs.extend([
            "-sdir",
            params.get("sdir")
        ])
    if params.get("white") is not None:
        cargs.extend([
            "-white",
            params.get("white")
        ])
    if params.get("pial") is not None:
        cargs.extend([
            "-pial",
            params.get("pial")
        ])
    if params.get("normalize_flag"):
        cargs.append("-normalize")
    if params.get("mean") is not None:
        cargs.extend([
            "-mean",
            params.get("mean")
        ])
    if params.get("xform") is not None:
        cargs.extend([
            "-xform",
            execution.input_file(params.get("xform"))
        ])
    if params.get("src") is not None:
        cargs.extend([
            "-src",
            execution.input_file(params.get("src"))
        ])
    if params.get("dst") is not None:
        cargs.extend([
            "-dst",
            execution.input_file(params.get("dst"))
        ])
    if params.get("invert_flag"):
        cargs.append("-invert")
    return cargs


def mris_intensity_profile_outputs(
    params: MrisIntensityProfileParameters,
    execution: Execution,
) -> MrisIntensityProfileOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisIntensityProfileOutputs(
        root=execution.output_file("."),
        output_curvature_file=execution.output_file(params.get("output_file")),
        output_mean_profile_integral=execution.output_file(params.get("mean")) if (params.get("mean") is not None) else None,
    )
    return ret


def mris_intensity_profile_execute(
    params: MrisIntensityProfileParameters,
    execution: Execution,
) -> MrisIntensityProfileOutputs:
    """
    This program computes the intensity profile of the cortical ribbon and writes
    the resulting measurement into a 'curvature' file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisIntensityProfileOutputs`).
    """
    params = execution.params(params)
    cargs = mris_intensity_profile_cargs(params, execution)
    ret = mris_intensity_profile_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_intensity_profile(
    subject_name: str,
    hemi: str,
    volume: InputPathType,
    output_file: str,
    write_surf: str | None = None,
    sdir: str | None = None,
    white: str | None = None,
    pial: str | None = None,
    normalize_flag: bool = False,
    mean: str | None = None,
    xform: InputPathType | None = None,
    src: InputPathType | None = None,
    dst: InputPathType | None = None,
    invert_flag: bool = False,
    runner: Runner | None = None,
) -> MrisIntensityProfileOutputs:
    """
    This program computes the intensity profile of the cortical ribbon and writes
    the resulting measurement into a 'curvature' file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Name of the subject.
        hemi: Hemisphere (e.g. lh or rh).
        volume: Volume file to be processed.
        output_file: Output file where the measurement is saved.
        write_surf: Write the variational pial surface target locations.
        sdir: Specifies the SUBJECTS_DIR.
        white: Specifies the WHITE surface filename.
        pial: Specifies the PIAL surface filename.
        normalize_flag: Normalized sampling with respect to thickness.
        mean: Outputs the mean profile-integral to the specified file (output\
            is in curv format).
        xform: Specify the registration transformation that maps the T1 volume\
            to the input volume to be sampled.
        src: Source volume used when computing the registration transformation.
        dst: Destination volume used when computing the registration\
            transformation.
        invert_flag: Apply the registration transformation inversely.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisIntensityProfileOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_INTENSITY_PROFILE_METADATA)
    params = mris_intensity_profile_params(
        subject_name=subject_name,
        hemi=hemi,
        volume=volume,
        output_file=output_file,
        write_surf=write_surf,
        sdir=sdir,
        white=white,
        pial=pial,
        normalize_flag=normalize_flag,
        mean=mean,
        xform=xform,
        src=src,
        dst=dst,
        invert_flag=invert_flag,
    )
    return mris_intensity_profile_execute(params, execution)


__all__ = [
    "MRIS_INTENSITY_PROFILE_METADATA",
    "MrisIntensityProfileOutputs",
    "MrisIntensityProfileParameters",
    "mris_intensity_profile",
    "mris_intensity_profile_params",
]
