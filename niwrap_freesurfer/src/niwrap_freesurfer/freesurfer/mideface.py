# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MIDEFACE_METADATA = Metadata(
    id="e4a7d1cf3f8f93ccdd73f64b12dba5ce0fe4110b.boutiques",
    name="mideface",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MidefaceParameters = typing.TypedDict('MidefaceParameters', {
    "__STYX_TYPE__": typing.Literal["mideface"],
    "input_volume": InputPathType,
    "output_volume": str,
    "facemask": typing.NotRequired[InputPathType | None],
    "output_dir": typing.NotRequired[str | None],
    "exclusion_mask": typing.NotRequired[InputPathType | None],
    "samseg_ndilations": typing.NotRequired[float | None],
    "samseg_json": typing.NotRequired[str | None],
    "samseg_fast": bool,
    "no_samseg_fast": bool,
    "init_reg": typing.NotRequired[InputPathType | None],
    "synthseg_ndilations": typing.NotRequired[float | None],
    "fill_const": typing.NotRequired[list[float] | None],
    "fill_zero": bool,
    "fhi": typing.NotRequired[float | None],
    "no_ears": bool,
    "back_of_head": bool,
    "forehead": bool,
    "pics": bool,
    "code": typing.NotRequired[str | None],
    "image_convert": typing.NotRequired[str | None],
    "no_post": bool,
    "threads": typing.NotRequired[float | None],
    "force": bool,
    "output_format": typing.NotRequired[str | None],
    "atlas": typing.NotRequired[str | None],
    "expert": typing.NotRequired[str | None],
    "display_no": typing.NotRequired[float | None],
    "apply_volume": typing.NotRequired[str | None],
    "check_volume": typing.NotRequired[InputPathType | None],
    "check_output_file": typing.NotRequired[InputPathType | None],
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
        "mideface": mideface_cargs,
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
        "mideface": mideface_outputs,
    }.get(t)


class MidefaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mideface(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    defaced_output: OutputPathType
    """Defaced output volume"""
    facemask_output: OutputPathType | None
    """Applied facemask file"""


def mideface_params(
    input_volume: InputPathType,
    output_volume: str,
    facemask: InputPathType | None = None,
    output_dir: str | None = None,
    exclusion_mask: InputPathType | None = None,
    samseg_ndilations: float | None = None,
    samseg_json: str | None = None,
    samseg_fast: bool = False,
    no_samseg_fast: bool = False,
    init_reg: InputPathType | None = None,
    synthseg_ndilations: float | None = None,
    fill_const: list[float] | None = None,
    fill_zero: bool = False,
    fhi: float | None = None,
    no_ears: bool = False,
    back_of_head: bool = False,
    forehead: bool = False,
    pics: bool = False,
    code_: str | None = None,
    image_convert: str | None = None,
    no_post: bool = False,
    threads: float | None = None,
    force: bool = False,
    output_format: str | None = None,
    atlas: str | None = None,
    expert: str | None = None,
    display_no: float | None = None,
    apply_volume: str | None = None,
    check_volume: InputPathType | None = None,
    check_output_file: InputPathType | None = None,
) -> MidefaceParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Volume to deface.
        output_volume: Defaced output volume.
        facemask: Facemask to apply.
        output_dir: Directory for outputs, activates PostHeadSurf.
        exclusion_mask: Mask to exclude certain regions from defacing.
        samseg_ndilations: Number of dilations for Samseg segmentation.
        samseg_json: JSON configuration for Samseg.
        samseg_fast: Configure Samseg to run quickly.
        no_samseg_fast: Do not configure Samseg to run quickly.
        init_reg: Initial registration file for Samseg.
        synthseg_ndilations: Number of dilations for Synthseg segmentation.
        fill_const: Constants for filling regions.
        fill_zero: Fill regions with zero.
        fhi: FHI value for MRIchangeType().
        no_ears: Do not include ears in the defacing.
        back_of_head: Include back of head in defacing.
        forehead: Include forehead in defacing (risks removing brain).
        pics: Take pictures of the defaced result.
        code_: Embed code name in pictures.
        image_convert: Path to ImageMagick convert binary for pictures.
        no_post: Do not make a head surface after defacing.
        threads: Number of threads to use.
        force: Force reprocessing (only applicable if output directory is used).
        output_format: Output file format.
        atlas: Directory containing atlas files.
        expert: Additional expert options.
        display_no: Xvfb display number for taking pictures.
        apply_volume: Apply midface output to a second volume.
        check_volume: Volume to check if defaced.
        check_output_file: Optional output file for check result.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mideface",
        "input_volume": input_volume,
        "output_volume": output_volume,
        "samseg_fast": samseg_fast,
        "no_samseg_fast": no_samseg_fast,
        "fill_zero": fill_zero,
        "no_ears": no_ears,
        "back_of_head": back_of_head,
        "forehead": forehead,
        "pics": pics,
        "no_post": no_post,
        "force": force,
    }
    if facemask is not None:
        params["facemask"] = facemask
    if output_dir is not None:
        params["output_dir"] = output_dir
    if exclusion_mask is not None:
        params["exclusion_mask"] = exclusion_mask
    if samseg_ndilations is not None:
        params["samseg_ndilations"] = samseg_ndilations
    if samseg_json is not None:
        params["samseg_json"] = samseg_json
    if init_reg is not None:
        params["init_reg"] = init_reg
    if synthseg_ndilations is not None:
        params["synthseg_ndilations"] = synthseg_ndilations
    if fill_const is not None:
        params["fill_const"] = fill_const
    if fhi is not None:
        params["fhi"] = fhi
    if code_ is not None:
        params["code"] = code_
    if image_convert is not None:
        params["image_convert"] = image_convert
    if threads is not None:
        params["threads"] = threads
    if output_format is not None:
        params["output_format"] = output_format
    if atlas is not None:
        params["atlas"] = atlas
    if expert is not None:
        params["expert"] = expert
    if display_no is not None:
        params["display_no"] = display_no
    if apply_volume is not None:
        params["apply_volume"] = apply_volume
    if check_volume is not None:
        params["check_volume"] = check_volume
    if check_output_file is not None:
        params["check_output_file"] = check_output_file
    return params


def mideface_cargs(
    params: MidefaceParameters,
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
    cargs.append("mideface")
    cargs.extend([
        "--i",
        execution.input_file(params.get("input_volume"))
    ])
    cargs.extend([
        "--o",
        params.get("output_volume")
    ])
    if params.get("facemask") is not None:
        cargs.extend([
            "--facemask",
            execution.input_file(params.get("facemask"))
        ])
    if params.get("output_dir") is not None:
        cargs.extend([
            "--odir",
            params.get("output_dir")
        ])
    if params.get("exclusion_mask") is not None:
        cargs.extend([
            "--xmask",
            execution.input_file(params.get("exclusion_mask"))
        ])
    if params.get("samseg_ndilations") is not None:
        cargs.extend([
            "--xmask-samseg",
            str(params.get("samseg_ndilations"))
        ])
    if params.get("samseg_json") is not None:
        cargs.extend([
            "--samseg-json",
            params.get("samseg_json")
        ])
    if params.get("samseg_fast"):
        cargs.append("--samseg-fast")
    if params.get("no_samseg_fast"):
        cargs.append("--no-samseg-fast")
    if params.get("init_reg") is not None:
        cargs.extend([
            "--init-reg",
            execution.input_file(params.get("init_reg"))
        ])
    if params.get("synthseg_ndilations") is not None:
        cargs.extend([
            "--xmask-synthseg",
            str(params.get("synthseg_ndilations"))
        ])
    if params.get("fill_const") is not None:
        cargs.extend([
            "--fill-const",
            *map(str, params.get("fill_const"))
        ])
    if params.get("fill_zero"):
        cargs.append("--fill-zero")
    if params.get("fhi") is not None:
        cargs.extend([
            "--fhi",
            str(params.get("fhi"))
        ])
    if params.get("no_ears"):
        cargs.append("--no-ears")
    if params.get("back_of_head"):
        cargs.append("--back-of-head")
    if params.get("forehead"):
        cargs.append("--forehead")
    if params.get("pics"):
        cargs.append("--pics")
    if params.get("code") is not None:
        cargs.extend([
            "--code",
            params.get("code")
        ])
    if params.get("image_convert") is not None:
        cargs.extend([
            "--imconvert",
            params.get("image_convert")
        ])
    if params.get("no_post"):
        cargs.append("--no-post")
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("force"):
        cargs.append("--force")
    if params.get("output_format") is not None:
        cargs.extend([
            "--nii --nii.gz --mgz",
            params.get("output_format")
        ])
    if params.get("atlas") is not None:
        cargs.extend([
            "--atlas",
            params.get("atlas")
        ])
    if params.get("expert") is not None:
        cargs.extend([
            "--expert",
            params.get("expert")
        ])
    if params.get("display_no") is not None:
        cargs.extend([
            "--display",
            str(params.get("display_no"))
        ])
    if params.get("apply_volume") is not None:
        cargs.extend([
            "--apply",
            params.get("apply_volume")
        ])
    if params.get("check_volume") is not None:
        cargs.extend([
            "--check",
            execution.input_file(params.get("check_volume"))
        ])
    if params.get("check_output_file") is not None:
        cargs.extend([
            "--check",
            execution.input_file(params.get("check_output_file"))
        ])
    return cargs


def mideface_outputs(
    params: MidefaceParameters,
    execution: Execution,
) -> MidefaceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MidefaceOutputs(
        root=execution.output_file("."),
        defaced_output=execution.output_file(params.get("output_volume")),
        facemask_output=execution.output_file(pathlib.Path(params.get("facemask")).name) if (params.get("facemask") is not None) else None,
    )
    return ret


def mideface_execute(
    params: MidefaceParameters,
    execution: Execution,
) -> MidefaceOutputs:
    """
    Minimally invasive defacing tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MidefaceOutputs`).
    """
    params = execution.params(params)
    cargs = mideface_cargs(params, execution)
    ret = mideface_outputs(params, execution)
    execution.run(cargs)
    return ret


def mideface(
    input_volume: InputPathType,
    output_volume: str,
    facemask: InputPathType | None = None,
    output_dir: str | None = None,
    exclusion_mask: InputPathType | None = None,
    samseg_ndilations: float | None = None,
    samseg_json: str | None = None,
    samseg_fast: bool = False,
    no_samseg_fast: bool = False,
    init_reg: InputPathType | None = None,
    synthseg_ndilations: float | None = None,
    fill_const: list[float] | None = None,
    fill_zero: bool = False,
    fhi: float | None = None,
    no_ears: bool = False,
    back_of_head: bool = False,
    forehead: bool = False,
    pics: bool = False,
    code_: str | None = None,
    image_convert: str | None = None,
    no_post: bool = False,
    threads: float | None = None,
    force: bool = False,
    output_format: str | None = None,
    atlas: str | None = None,
    expert: str | None = None,
    display_no: float | None = None,
    apply_volume: str | None = None,
    check_volume: InputPathType | None = None,
    check_output_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> MidefaceOutputs:
    """
    Minimally invasive defacing tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Volume to deface.
        output_volume: Defaced output volume.
        facemask: Facemask to apply.
        output_dir: Directory for outputs, activates PostHeadSurf.
        exclusion_mask: Mask to exclude certain regions from defacing.
        samseg_ndilations: Number of dilations for Samseg segmentation.
        samseg_json: JSON configuration for Samseg.
        samseg_fast: Configure Samseg to run quickly.
        no_samseg_fast: Do not configure Samseg to run quickly.
        init_reg: Initial registration file for Samseg.
        synthseg_ndilations: Number of dilations for Synthseg segmentation.
        fill_const: Constants for filling regions.
        fill_zero: Fill regions with zero.
        fhi: FHI value for MRIchangeType().
        no_ears: Do not include ears in the defacing.
        back_of_head: Include back of head in defacing.
        forehead: Include forehead in defacing (risks removing brain).
        pics: Take pictures of the defaced result.
        code_: Embed code name in pictures.
        image_convert: Path to ImageMagick convert binary for pictures.
        no_post: Do not make a head surface after defacing.
        threads: Number of threads to use.
        force: Force reprocessing (only applicable if output directory is used).
        output_format: Output file format.
        atlas: Directory containing atlas files.
        expert: Additional expert options.
        display_no: Xvfb display number for taking pictures.
        apply_volume: Apply midface output to a second volume.
        check_volume: Volume to check if defaced.
        check_output_file: Optional output file for check result.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MidefaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MIDEFACE_METADATA)
    params = mideface_params(
        input_volume=input_volume,
        output_volume=output_volume,
        facemask=facemask,
        output_dir=output_dir,
        exclusion_mask=exclusion_mask,
        samseg_ndilations=samseg_ndilations,
        samseg_json=samseg_json,
        samseg_fast=samseg_fast,
        no_samseg_fast=no_samseg_fast,
        init_reg=init_reg,
        synthseg_ndilations=synthseg_ndilations,
        fill_const=fill_const,
        fill_zero=fill_zero,
        fhi=fhi,
        no_ears=no_ears,
        back_of_head=back_of_head,
        forehead=forehead,
        pics=pics,
        code_=code_,
        image_convert=image_convert,
        no_post=no_post,
        threads=threads,
        force=force,
        output_format=output_format,
        atlas=atlas,
        expert=expert,
        display_no=display_no,
        apply_volume=apply_volume,
        check_volume=check_volume,
        check_output_file=check_output_file,
    )
    return mideface_execute(params, execution)


__all__ = [
    "MIDEFACE_METADATA",
    "MidefaceOutputs",
    "MidefaceParameters",
    "mideface",
    "mideface_params",
]
