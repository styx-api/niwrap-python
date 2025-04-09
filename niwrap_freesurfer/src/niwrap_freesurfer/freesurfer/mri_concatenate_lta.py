# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_CONCATENATE_LTA_METADATA = Metadata(
    id="954e185b276c52b9e741616fe3781dbd26c9152a.boutiques",
    name="mri_concatenate_lta",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriConcatenateLtaParameters = typing.TypedDict('MriConcatenateLtaParameters', {
    "__STYX_TYPE__": typing.Literal["mri_concatenate_lta"],
    "lta_1": InputPathType,
    "lta_2": InputPathType,
    "lta_final": str,
    "tal_src": typing.NotRequired[InputPathType | None],
    "tal_template": typing.NotRequired[InputPathType | None],
    "invert1": bool,
    "invert2": bool,
    "invertout": bool,
    "out_type": typing.NotRequired[float | None],
    "subject": typing.NotRequired[str | None],
    "rmsdiff_radius": typing.NotRequired[float | None],
    "rmsdiff_outputfile": typing.NotRequired[str | None],
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
        "mri_concatenate_lta": mri_concatenate_lta_cargs,
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
    }.get(t)


class MriConcatenateLtaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_concatenate_lta(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_concatenate_lta_params(
    lta_1: InputPathType,
    lta_2: InputPathType,
    lta_final: str,
    tal_src: InputPathType | None = None,
    tal_template: InputPathType | None = None,
    invert1: bool = False,
    invert2: bool = False,
    invertout: bool = False,
    out_type: float | None = None,
    subject: str | None = None,
    rmsdiff_radius: float | None = None,
    rmsdiff_outputfile: str | None = None,
) -> MriConcatenateLtaParameters:
    """
    Build parameters.
    
    Args:
        lta_1: File for LTA transformation that maps some src1 to dst1.
        lta_2: File for LTA transformation that maps dst1 (src2) to dst2.
        lta_final: File for the combined LTA maps: src1 to dst2 = LTA2*LTA1.
        tal_src: Specify source (file1) for Talairach transformation.
        tal_template: Specify template (file2) for Talairach transformation.
        invert1: Invert LTA1 before applying it.
        invert2: Invert LTA2 before applying it.
        invertout: Invert output LTA.
        out_type: Set final LTA type: 0 for VOX2VOX (default), 1 for RAS2RAS.
        subject: Set subject in output LTA.
        rmsdiff_radius: Radius used for computing RMS diff between transforms.
        rmsdiff_outputfile: Output file for RMS diff computation. Use 'nofile'\
            to skip output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_concatenate_lta",
        "lta_1": lta_1,
        "lta_2": lta_2,
        "lta_final": lta_final,
        "invert1": invert1,
        "invert2": invert2,
        "invertout": invertout,
    }
    if tal_src is not None:
        params["tal_src"] = tal_src
    if tal_template is not None:
        params["tal_template"] = tal_template
    if out_type is not None:
        params["out_type"] = out_type
    if subject is not None:
        params["subject"] = subject
    if rmsdiff_radius is not None:
        params["rmsdiff_radius"] = rmsdiff_radius
    if rmsdiff_outputfile is not None:
        params["rmsdiff_outputfile"] = rmsdiff_outputfile
    return params


def mri_concatenate_lta_cargs(
    params: MriConcatenateLtaParameters,
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
    cargs.append("mri_concatenate_lta")
    cargs.append(execution.input_file(params.get("lta_1")))
    cargs.append(execution.input_file(params.get("lta_2")))
    cargs.append(params.get("lta_final"))
    if params.get("tal_src") is not None:
        cargs.extend([
            "-tal",
            execution.input_file(params.get("tal_src"))
        ])
    if params.get("tal_template") is not None:
        cargs.append(execution.input_file(params.get("tal_template")))
    if params.get("invert1"):
        cargs.append("-invert1")
    if params.get("invert2"):
        cargs.append("-invert2")
    if params.get("invertout"):
        cargs.append("-invertout")
    if params.get("out_type") is not None:
        cargs.extend([
            "-out_type",
            str(params.get("out_type"))
        ])
    if params.get("subject") is not None:
        cargs.extend([
            "-subject",
            params.get("subject")
        ])
    if params.get("rmsdiff_radius") is not None:
        cargs.extend([
            "-rmsdiff",
            str(params.get("rmsdiff_radius"))
        ])
    if params.get("rmsdiff_outputfile") is not None:
        cargs.append(params.get("rmsdiff_outputfile"))
    return cargs


def mri_concatenate_lta_outputs(
    params: MriConcatenateLtaParameters,
    execution: Execution,
) -> MriConcatenateLtaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriConcatenateLtaOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_concatenate_lta_execute(
    params: MriConcatenateLtaParameters,
    execution: Execution,
) -> MriConcatenateLtaOutputs:
    """
    Concatenates two consecutive LTA transformations into one overall
    transformation, Out = LTA2*LTA1.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriConcatenateLtaOutputs`).
    """
    params = execution.params(params)
    cargs = mri_concatenate_lta_cargs(params, execution)
    ret = mri_concatenate_lta_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_concatenate_lta(
    lta_1: InputPathType,
    lta_2: InputPathType,
    lta_final: str,
    tal_src: InputPathType | None = None,
    tal_template: InputPathType | None = None,
    invert1: bool = False,
    invert2: bool = False,
    invertout: bool = False,
    out_type: float | None = None,
    subject: str | None = None,
    rmsdiff_radius: float | None = None,
    rmsdiff_outputfile: str | None = None,
    runner: Runner | None = None,
) -> MriConcatenateLtaOutputs:
    """
    Concatenates two consecutive LTA transformations into one overall
    transformation, Out = LTA2*LTA1.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        lta_1: File for LTA transformation that maps some src1 to dst1.
        lta_2: File for LTA transformation that maps dst1 (src2) to dst2.
        lta_final: File for the combined LTA maps: src1 to dst2 = LTA2*LTA1.
        tal_src: Specify source (file1) for Talairach transformation.
        tal_template: Specify template (file2) for Talairach transformation.
        invert1: Invert LTA1 before applying it.
        invert2: Invert LTA2 before applying it.
        invertout: Invert output LTA.
        out_type: Set final LTA type: 0 for VOX2VOX (default), 1 for RAS2RAS.
        subject: Set subject in output LTA.
        rmsdiff_radius: Radius used for computing RMS diff between transforms.
        rmsdiff_outputfile: Output file for RMS diff computation. Use 'nofile'\
            to skip output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriConcatenateLtaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CONCATENATE_LTA_METADATA)
    params = mri_concatenate_lta_params(
        lta_1=lta_1,
        lta_2=lta_2,
        lta_final=lta_final,
        tal_src=tal_src,
        tal_template=tal_template,
        invert1=invert1,
        invert2=invert2,
        invertout=invertout,
        out_type=out_type,
        subject=subject,
        rmsdiff_radius=rmsdiff_radius,
        rmsdiff_outputfile=rmsdiff_outputfile,
    )
    return mri_concatenate_lta_execute(params, execution)


__all__ = [
    "MRI_CONCATENATE_LTA_METADATA",
    "MriConcatenateLtaOutputs",
    "MriConcatenateLtaParameters",
    "mri_concatenate_lta",
    "mri_concatenate_lta_params",
]
